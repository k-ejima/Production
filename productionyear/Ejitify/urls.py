from django.urls import path
from . import views

app_name = 'Ejitify'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('artist/', views.ArtistView.as_view(), name='artist'),
    path('genre/', views.GenreView.as_view(), name='genre'),
    path('search/', views.SearchView.as_view(), name='search'),
]