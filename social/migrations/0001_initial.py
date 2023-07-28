# Generated by Django 4.2.3 on 2023-07-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebooksvg', models.ImageField(upload_to='')),
                ('facebooklink', models.URLField()),
                ('linkedinsvg', models.ImageField(upload_to='')),
                ('linkedinlink', models.URLField()),
                ('instagramsvg', models.ImageField(upload_to='')),
                ('instagramlink', models.URLField()),
                ('youtubesvg', models.ImageField(upload_to='')),
                ('youtubelink', models.URLField()),
            ],
        ),
    ]