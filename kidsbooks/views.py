from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import KidsbookForm, ReviewForm
from .models import Kidsbook, Review

# Create your views here.
def kidsbook_list(request):
    kidsbooks = Kidsbook.objects.all()
    print(kidsbooks)
    context = {
        'kidsbooks': kidsbooks
    }
    return render(request, 'kidsbooks/viewlist.html', context)
