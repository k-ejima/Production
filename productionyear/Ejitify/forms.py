from django import forms
from .models import Playlist

class SearchForm(forms.Form):
    query = forms.CharField(label='検索', max_length=100)

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']
        labels = {
            'name': 'プレイリストの名前',
            'songs': '曲一覧'
        }
        widgets = {
            'songs': forms.CheckboxSelectMultiple()
        }