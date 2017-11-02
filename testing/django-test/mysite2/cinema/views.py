# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Screening

# Create your views here.

def index(request):
    showing_movies_list = (Movie.objects.filter(id__in=[s.movie_id for s in Screening.objects.all().distinct()]))
    context = {'showing_movies_list': showing_movies_list}
    return render(request, 'cinema/index.html', context)

def detail(request, movie_id):
    movie = Movie.objects.filter(id=movie_id)
    context = {'movie': movie[0]}
    return render(request, 'cinema/movie.html', context)
    