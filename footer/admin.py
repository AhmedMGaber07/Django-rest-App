from django.contrib import admin

from .models import Certificate

# Register your models here.


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_per_page = 20
