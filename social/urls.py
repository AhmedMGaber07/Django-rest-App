from django.urls import path
from . import views

# from rest_framework_simplejwt.views import (
#   TokenObtainPairView,
# TokenRefreshView,)


urlpatterns = [
    path('social/<str:id>', views.SocialDetails.as_view()),
    path('', views.social_list),
]
