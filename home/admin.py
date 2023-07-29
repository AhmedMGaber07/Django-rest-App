from django.contrib import admin

from .models import *
# Register your models here.


class AboutUsInline(admin.StackedInline):
    model = AboutUs


class ProjectInline(admin.StackedInline):
    model = Project


class ProjectsValueInline(admin.StackedInline):
    model = ProjectsValue


class ProjectsAreaInline(admin.StackedInline):
    model = ProjectsArea


class ProjectsPaybackInline(admin.StackedInline):
    model = ProjectsPayback


class ProjectsExperienceInline(admin.StackedInline):
    model = ProjectsExperience


class ProjectsGrowingInline(admin.StackedInline):
    model = ProjectsGrowing


class CreateValueInline(admin.StackedInline):
    model = CreateValue


class ServiceInline(admin.StackedInline):
    model = Service


class ContactUsInline(admin.StackedInline):
    model = ContactUs


class HeroSliderInline(admin.StackedInline):
    model = HeroSlider


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [
        AboutUsInline, ProjectInline, ProjectsValueInline, ProjectsAreaInline, ProjectsPaybackInline,
        ProjectsExperienceInline, ProjectsGrowingInline, CreateValueInline, ServiceInline, ContactUsInline, HeroSliderInline]

    def has_add_permission(self, request, obj=None):
        count = Hero.objects.count()
        if count == 1:
            return False
        else:
            return True
