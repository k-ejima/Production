from django.contrib import admin

# Register your models here.


from .models import Category,PhotoArtist,Song,Playlist

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('namecategory', 'imagecategory')
admin.site.register(Category, CategoryAdmin)

class SongInline(admin.TabularInline):
    model = Song
    extra = 1
admin.site.register(Song)

class PhotoArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'category', 'user')
    inlines = [SongInline]
admin.site.register(PhotoArtist, PhotoArtistAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
admin.site.register(Playlist, PlaylistAdmin)