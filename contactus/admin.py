from django.contrib import admin

# Register your models here.

from .models import ContactUs, ContactForm


@admin.register(ContactUs)
class ContuctUsAdmin(admin.ModelAdmin):
    list_per_page = 20

    # This will help you to disbale add functionality

    def has_add_permission(self, request, obj=None):
        count = ContactUs.objects.count()
        if count == 1:
            return False
        else:
            return True


@admin.register(ContactForm)
class ContuctFormAdmin(admin.ModelAdmin):
    list_per_page = 20

    # This will help you to disbale add functionality
