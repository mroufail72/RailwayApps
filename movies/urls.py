""" URLS """
from django.urls import path
from . import views

# movies/ (root)
# movies/1/details
# /old_system/movies/1/details

app_name = 'movies'  # add this so we don't have to add "movies_" prefix in code

# urlpatterns = [
#     path('', views.index, name='movies_index'),  # root
#     path('<int:movie_id>', views.detail, name='movies_detail'),  # root
# ]

urlpatterns = [
    path('', views.index, name='index'),  # root
    path('<int:movie_id>', views.detail, name='detail'),  # root
    path('export', views.expProd, name='export')

]
