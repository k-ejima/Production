from django.shortcuts import render
from django.views.generic import TemplateView,ListView

from .models import PhotoArtist
from .forms import SearchForm

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoArtist.objects.order_by('artist_name')

class ArtistView(ListView):
    model = PhotoArtist
    template_name = 'artist.html'
    context_object_name = 'artist'

class GenreView(TemplateView):
    template_name = 'genre.html'

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