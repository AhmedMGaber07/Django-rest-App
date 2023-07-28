from django.db import models

# Create your models here.


class Social(models.Model):
    facebooksvg = models.ImageField(null=False, blank=False)
    facebooklink = models.URLField(max_length=200, null=False, blank=False)

    linkedinsvg = models.ImageField(null=False, blank=False)
    linkedinlink = models.URLField(max_length=200, null=False, blank=False)

    instagramsvg = models.ImageField(null=False, blank=False)
    instagramlink = models.URLField(max_length=200, null=False, blank=False)

    youtubesvg = models.ImageField(null=False, blank=False)
    youtubelink = models.URLField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.facebooklink   