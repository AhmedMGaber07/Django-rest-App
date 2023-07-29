from django.db import models

# Create your models here.


class Hero(models.Model):
    title = models.TextField(max_length=250)
    title_highlighted = models.TextField(max_length=250)

    def __str__(self):
        return 'Home'

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"


class HeroSlider(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    hero_contant = models.TextField(max_length=250)
    hero_video_or_image = models.FileField(upload_to='documents/')
    order = models.DecimalField(max_digits=10, decimal_places=0, default='')

    def __str__(self):
        return 'Hero Slider'

    class Meta:
        verbose_name = "Hero Slider"
        verbose_name_plural = "Hero Slider"


class AboutUs(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    content = models.TextField(max_length=250)
    photo = models.ImageField(upload_to='documents/')
    btn = models.TextField(max_length=250)

    def __str__(self):
        return 'AboutUs'

    class Meta:
        verbose_name = "AboutUs"
        verbose_name_plural = "AboutUs"


class Project(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    title_highlighted = models.TextField(max_length=250)
    # changed when create projects in services&Projects project

    btn = models.TextField(max_length=250)

    def __str__(self):
        return 'Projects'

    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"


class ProjectsValue(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    number = models.DecimalField(
        max_digits=10, decimal_places=0, default='')

    def __str__(self):
        return 'Projects Value'

    class Meta:
        verbose_name = "Projects Value"
        verbose_name_plural = "Projects Value"


class ProjectsArea(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    number = models.DecimalField(
        max_digits=10, decimal_places=0, default='')

    def __str__(self):
        return 'Projects Area'

    class Meta:
        verbose_name = "Projects Area"
        verbose_name_plural = "Projects Area"


class ProjectsPayback(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    number = models.DecimalField(
        max_digits=10, decimal_places=0, default='')

    def __str__(self):
        return 'Projects Payback'

    class Meta:
        verbose_name = "Projects Payback"
        verbose_name_plural = "Projects Payback"


class ProjectsExperience(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    number = models.DecimalField(
        max_digits=10, decimal_places=0, default='')
    description = models.TextField(max_length=250)

    def __str__(self):
        return 'Projects Experience'

    class Meta:
        verbose_name = "Projects Experience"
        verbose_name_plural = "Projects Experience"


class ProjectsGrowing(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    number = models.DecimalField(
        max_digits=10, decimal_places=0, default='')
    description = models.TextField(max_length=250)

    def __str__(self):
        return 'Projects Growing'

    class Meta:
        verbose_name = "Projects Growing"
        verbose_name_plural = "Projects Growing"


class CreateValue(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    description = models.TextField(max_length=250)

    def __str__(self):
        return 'Create Value'

    class Meta:
        verbose_name = "Create Value"
        verbose_name_plural = "Create Value"


class Service(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    btn = models.TextField(max_length=250)

# changed when create projects in services&Projects service

    def __str__(self):
        return 'Service'

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Service"


class ContactUs(models.Model):
    hero = models.ForeignKey(
        Hero, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=250)
    title_highlighted = models.TextField(max_length=250)
    logo = models.ImageField(upload_to='documents/')
    btn = models.TextField(max_length=250)

    def __str__(self):
        return 'Contact Us'

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
