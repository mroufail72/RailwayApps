"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from api.models import MovieResource
import api.models
from . import views

movie_resource = api.models.MovieResource()

urlpatterns = [
    # path('', views.home),
    path('', views.showlist, name='showlist'),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls)),
    # path('movies/', include('movies.urls'), views.showlist, name='showlist')

]

admin.site.site_header = "Vidly Admin"
admin.site.site_title = "Vidly Admin Portal"
admin.site.index_title = "Welcome to Vidly Portal"
