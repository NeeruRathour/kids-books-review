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

def index(request):
    books = Kidsbook.objects.all()  
    return render(request, 'home/index.html', {'books': books})

def about_us(request):
    return render(request, 'aboutus.html')


def kidsbook_list(request):
    kidsbooks = Kidsbook.objects.all()

    # Calculate average rating for each book
    for book in kidsbooks:
        book.average_rating = book.ratings.aggregate(average_rating=Avg('rating'))['average_rating'] or 0.0

    context = {
        'kidsbooks': kidsbooks
    }
    return render(request, 'kidsbooks/viewlist.html', context)


def kidsbook_detail(request, id):
    kidsbook = get_object_or_404(Kidsbook, id=id)
    reviews = kidsbook.kidsbook_reviews.all()

    # Calculate average rating for the book
    average_rating = kidsbook.ratings.aggregate(Avg('rating'))['rating__avg'] or 0.0

    if request.method == "POST" and request.user.is_authenticated:
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = kidsbook
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted successfully.')
            # After submitting the review, recalculate the average rating
            average_rating = kidsbook.ratings.aggregate(Avg('rating'))['rating__avg'] or 0.0
        return redirect('kidsbook_detail', id=id)

    review_form = ReviewForm() if request.user.is_authenticated else None

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

                # Recalculate average rating
                average_rating = book.ratings.aggregate(Avg('rating'))['rating__avg'] or 0.0

                # Update context and redirect
                return HttpResponseRedirect(reverse('kidsbook_detail', args=[book_id]))

        except ValueError:
            pass
        
    context = {
        'book': book
    }
    return render(request, 'kidsbooks/rate_book.html', context)




@login_required
def my_reviews(request):
    try:
        # Fetch reviews for the current user and order by 'created_on'
        reviews = Review.objects.filter(user=request.user).order_by('-created_on')
        
        # Calculate average rating for each book associated with the reviews
        for review in reviews:
            review.book.average_rating = review.book.ratings.aggregate(average_rating=Avg('rating'))['average_rating'] or 0.0
    
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        reviews = []

    context = {
        'reviews': reviews,
    }
    return render(request, 'kidsbooks/my_reviews.html', context)


