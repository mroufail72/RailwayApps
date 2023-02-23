from django.shortcuts import render
from movies.models import Movie
from movies.models import MovieList
# import movies.export_prod_db


def home(request):
    return render(request, 'home.html')


def showlist(request):
    results = Movie.objects.all
    return render(request, "home.html", {"showmovie": results})
