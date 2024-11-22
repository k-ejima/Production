from django.urls import path
from . import views

app_name = 'Ejitify'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('artist/', views.ArtistView.as_view(), name='artist'),
    path('genre/', views.GenreView.as_view(), name='genre'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('search/', views.SearchView.as_view(), name='search'),
]