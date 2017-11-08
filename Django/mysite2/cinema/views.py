# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Movie, Screening

# Create your views here.


def index(request):
    showing_movies_list = (Movie.objects.filter(
        id__in=[s.movie_id for s in Screening.objects.all().distinct()]))
    context = {'showing_movies_list': showing_movies_list}
    return render(request, 'cinema/index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.filter(id=movie_id)[0]
    screenings = Screening.objects.filter(movie_id=movie.id)
    for s in screenings:
        print s.id
    context = {'movie': movie, 'screenings': screenings}
    return render(request, 'cinema/movie.html', context)


def screening(request, screening_id):
    screening = Screening.objects.filter(pk=screening_id)[0]
    print screening
    movie = Movie.objects.filter(id=screening.movie_id)[0]
    context = {'screening': screening, 'movie': movie}
    return render(request, 'cinema/screening.html', context)
