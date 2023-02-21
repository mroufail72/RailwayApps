from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# import tastypie.resources
# import movies.models

# Create your models here.


# class MovieResource(tastypie.resources.ModelResource):
#     class Meta:
#         queryset = movies.models.Movie.objects.all()
#         resource_name = 'movies'
#         excludes = ['date_created']

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
