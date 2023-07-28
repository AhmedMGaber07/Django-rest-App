from django.contrib import admin

from .models import News,NewsTitle

# Register your models here.


class NewsTitleInline(admin.StackedInline):
    model = NewsTitle

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [NewsTitleInline]
