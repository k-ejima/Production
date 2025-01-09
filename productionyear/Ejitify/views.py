from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

from .models import PhotoArtist,Category
from .forms import SearchForm

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoArtist.objects.order_by('artist_name')

class ArtistView(DetailView):
    model = PhotoArtist
    template_name = 'artist.html'
    context_object_name = 'artist'

class GenreView(ListView):
    template_name = 'genre.html'
    model = Category
    context_object_name = 'categories'

class SearchView(ListView):
    model = PhotoArtist
    template_name = 'search.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return PhotoArtist.objects.filter(artist_name__icontains=query)
        return PhotoArtist.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET or None)
        return context