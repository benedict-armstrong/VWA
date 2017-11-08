# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Movie, Screening
from .forms import UserIdForm

# Create your views here.

def index(request):
    showing_movies_list = (Movie.objects.filter(id__in=[s.movie_id for s in Screening.objects.all().distinct()]))
    context = {'showing_movies_list': showing_movies_list}
    return render(request, 'cinema/index.html', context)

def detail(request, movie_id):
    movie = Movie.objects.filter(id=movie_id)[0]
    screenings = Screening.objects.filter(movie_id=movie.id)
    if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserIdForm()

    context = {'movie': movie, 'screenings': screenings, "form": form}

    return render(request, 'cinema/movie.html', context)
    