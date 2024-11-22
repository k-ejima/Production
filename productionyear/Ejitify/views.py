from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SignupView(TemplateView):
    template_name = 'signup.html'

class ArtistView(TemplateView):
    template_name = 'artist.html'

class GenreView(TemplateView):
    template_name = 'genre.html'

class LibraryView(TemplateView):
    template_name = 'library.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class SearchView(TemplateView):
    template_name = 'search.html'


