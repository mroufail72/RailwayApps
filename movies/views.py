"""VIEWS are the django equivalent to CONTROLLERS in MVC"""

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
from .models import MovieList

# Create your views here.


def index(request):
    """main page of an app.  The index function will be called by default """
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])  # LIST COMPREHENSION SYNTAX
    # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    # return HttpResponse("Hello World")
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})


# def detail(request, movie_id):
#     try:
#         movie = Movie.objects.get(pk=movie_id)
#         return render(request, 'movies/detail.html', {'movie': movie})
#     except Movie.DoesNotExist:
#         raise Http404()

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
