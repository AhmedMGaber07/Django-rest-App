from django.contrib import admin

# Register your models here.

from .models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_per_page = 20

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
