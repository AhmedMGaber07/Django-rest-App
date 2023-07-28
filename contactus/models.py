from django.db import models

# Create your models here.


class ContactUs(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.TextField(max_length=250)
    description = models.TextField(max_length=500, null=True, blank=True)
    logo = models.ImageField(null=False, blank=False)

    def __str__(self):
        return 'Contact US'

    class Meta:
        verbose_name = "Contuct Us"
        verbose_name_plural = "Contuct Us"


class ContactForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, null=True, blank=True)
    message = models.TextField(max_length=500)

    def __str__(self):
        return 'Contact form'

    class Meta:
        verbose_name = "Contuct form"
        verbose_name_plural = "Contuct form"
