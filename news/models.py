from django.db import models

# Create your models here.


class News(models.Model):
    title = models.TextField(max_length=250, default='')
    image = models.ImageField(upload_to='documents/', default='')
    short_description = models.TextField(max_length=500, default='')

    def __str__(self):
        return 'News'

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class NewsTitle(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.SET_NULL, null=True, blank=True)
    paragraph = models.TextField(max_length=250, default='')
    order = models.DecimalField(max_digits=10, decimal_places=0, default='')
    list_items = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return 'News descriptions'

    class Meta:
        verbose_name = "News description"
        verbose_name_plural = "News Title"
