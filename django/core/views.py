from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Movie, Person

# Create your views here.


class MovieDetail(DetailView):
    # model = Movie
    queryset = (Movie.objects.all_with_related_persons())


class MovieList(ListView):
    model = Movie
    paginate_by = 2


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()


class PersonList(ListView):
    model = Person
    paginate_by = 2

# Setting the order
