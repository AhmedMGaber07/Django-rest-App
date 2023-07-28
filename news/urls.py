from django.urls import path
from . import views


urlpatterns = [
    path('News/', views.News_Api.as_view()),

]
