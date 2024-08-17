from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.db.models import Avg 
from .forms import KidsbookForm, ReviewForm
from .models import Kidsbook, Review, Rating

# Create your views here.
def kidsbook_list(request):
    kidsbooks = Kidsbook.objects.all()

    for book in kidsbooks:
        book.average_rating = book.ratings.aggregate(Avg('rating'))['rating__avg']

    print(kidsbooks)
    context = {
        'kidsbooks': kidsbooks
    }
    return render(request, 'kidsbooks/viewlist.html', context)

def kidsbook_detail(request, id):
    kidsbook = get_object_or_404(Kidsbook, id=id)
    # reviews = Review.objects.filter(kidsbook=id)

    reviews = kidsbook.kidsbook_reviews.all()
    average_rating = kidsbook.ratings.aggregate(Avg('rating'))['rating__avg']


    # Save submitted review to the specific book and
    # send messages after submission
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = kidsbook
            review.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Review submitted and awaiting approval')
    review_form = ReviewForm()
    context = {
        'kidsbook': kidsbook,
        'reviews': reviews,
        'review_form': review_form,
        'average_rating': average_rating
    }
    return render(request, 'kidsbooks/viewdetail.html', context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.add_message(request, messages.SUCCESS, "Review updated successfully.")
            return redirect('kidsbook_detail', id=review.book.id)
    else:
        review_form = ReviewForm(instance=review)

    context = {
        'review_form': review_form,
        'review': review,
    }
    return render(request, 'kidsbooks/edit_review.html', context)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    # the user trying to delete the review is the author of the review
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")

    if request.method == "POST":
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Review deleted successfully.")
        return redirect('kidsbook_detail', id=review.book.id)

    context = {
        'review': review
    }
    return render(request, 'kidsbooks/delete_review.html', context)

@login_required
def rate_book(request, book_id):
    book = get_object_or_404(Kidsbook, id=book_id)

    if request.method == "POST":
        rating_value = request.POST.get("rating", "")

        try:
            rating_value = int(rating_value)
            if 1 <= rating_value <= 5:
                rating, created = Rating.objects.get_or_create(user=request.user, book=book)
                rating.rating = rating_value
                rating.save()
            
        except ValueError:
            
            pass
        
        return redirect('kidsbook_detail', id=book_id)

    context = {
        'book': book
    }
    return render(request, 'kidsbooks/rate_book.html', context)
