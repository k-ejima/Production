from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import PhotoArtist, Category, Playlist, Song
from .forms import SearchForm, PlaylistForm

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
        context['results'] = self.get_queryset()
        context['query'] = self.request.GET.get('query', '')
        return context

@login_required
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()
            return redirect('Ejitify:playlist_list')   
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form' : form})

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist_list.html'
    context_object_name = 'playlists'

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist_detail.html'
    context_object_name = 'playlist'

@login_required
def delete_playlist(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == 'POST':
        playlist.delete()
        return redirect('Ejitify:playlist_list')
