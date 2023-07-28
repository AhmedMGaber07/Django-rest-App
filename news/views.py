from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer

# Create your views here.


class News_Api(APIView):

    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
