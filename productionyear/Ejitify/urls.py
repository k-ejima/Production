from django.urls import path
from . import views

app_name = 'Ejitify'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('artist/<int:pk>', views.ArtistView.as_view(), name='artist'),
    path('genre/', views.GenreView.as_view(), name='genre'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('playlist/create/', views.create_playlist, name='create_playlist'),  
    path('playlists/', views.PlaylistListView.as_view(), name='playlist_list'), 
    path('playlist/<int:pk>', views.PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlist/<int:pk>/delete/', views.delete_playlist, name='playlist_delete'),

]
