from django.urls import path
from . import views


urlpatterns = [
    path('footer/certificate/', views.Footer_Api.as_view()),

]
