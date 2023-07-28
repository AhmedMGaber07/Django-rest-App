from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Certificate
from .serializers import CertificateSerializer

# Create your views here.


class Footer_Api(APIView):

    def get(self, request, format=None):
        certificate = Certificate.objects.all()
        serializer = CertificateSerializer(certificate, many=True)
        return Response(serializer.data)
