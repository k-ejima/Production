# Generated by Django 4.0 on 2024-12-22 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecategory', models.CharField(max_length=20, verbose_name='ジャンル')),
                ('imagecategory', models.ImageField(upload_to='photos', verbose_name='ジャンルの写真')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoArtist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200, verbose_name='アーティスト名')),
                ('comment', models.TextField(verbose_name='説明')),
                ('image1', models.ImageField(upload_to='photos', verbose_name='アーティスト写真小')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='アーティスト写真大')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ejitify.category', verbose_name='ジャンル')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200, verbose_name='曲のタイトル')),
                ('file', models.FileField(upload_to='songs', verbose_name='曲のファイル')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='Ejitify.photoartist', verbose_name='アーティスト')),
            ],
        ),
    ]
