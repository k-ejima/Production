from django.db import models

from accounts.models import CustomUser

class Category(models.Model):

    namecategory = models.CharField(
        verbose_name='ジャンル',
        max_length=20
    )

    imagecategory = models.ImageField(
        verbose_name='ジャンルの写真',
        upload_to='photos'
    )


    def __str__(self):

        return self.namecategory
    
class PhotoArtist(models.Model):

        user = models.ForeignKey(
            CustomUser,

            verbose_name='ユーザー',
            on_delete=models.CASCADE
        )

        category = models.ForeignKey(
            Category,

            verbose_name='ジャンル',

            on_delete=models.PROTECT
        )

        artist_name = models.CharField(
            verbose_name='アーティスト名',
            max_length=200
        )

        comment = models.TextField(
            verbose_name='説明',
        )

        image1 = models.ImageField(
            verbose_name='アーティスト写真小',
            upload_to='photos'
        )

        image2 = models.ImageField(
            verbose_name='アーティスト写真大',
            upload_to='photos',
            blank=True,
            null=True
        )

        def __str__(self):

            return self.artist_name
        
class Song(models.Model):
        artist = models.ForeignKey(
            PhotoArtist,
            verbose_name='アーティスト',
            on_delete=models.CASCADE,
            related_name='songs'
        )
        song_title = models.CharField(
            verbose_name='曲のタイトル',
            max_length=200
        )
        file = models.FileField(
            verbose_name='曲のファイル',
            upload_to='songs'
        )

        def __str__(self):
            return self.song_title