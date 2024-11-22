from django.db import models

# Create your models here.
class EjitifyArtist(models.Model):
    CATEGORY = (('New Release', 'ニューリリース'),
                ('Japanese', '邦楽'),
                ('Western', '洋楽'),
                ('Anime', 'アニメソング'),
                ('Enka', '演歌'),
                ('K-POP', 'K-POP'),
                ('classic', 'クラシック'),
                ('radio', 'ラジオ'))
    
    title = models.CharField(
        verbose_name='アーティスト',
        max_length=200
    )
    