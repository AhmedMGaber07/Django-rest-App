from django.db import models

# Create your models here.


class Certificate(models.Model):
    certificate = models.ImageField(upload_to='documents/', default='')
    pdf = models.FileField(upload_to='documents/', default='')

    def __str__(self):
        return 'Certificate'

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
