from django.urls import path
from . import views

# from rest_framework_simplejwt.views import (
#   TokenObtainPairView,
# TokenRefreshView,)


urlpatterns = [
    path('contact-us/', views.Contact_Us_Api.as_view()),
    path('contact-form/', views.Contact_Form_Api.as_view()),


]
