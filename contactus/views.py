from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import ContactUs, ContactForm
from .serializers import ContactUsSerializer, ContactFormSerializer

# Create your views here.


class Contact_Us_Api(APIView):

    def get_object(self, id):
        try:
            return ContactUs.objects.get(id=id)
        except ContactUs.DoesNotExist:
            raise Response('ContuctUs Does Not Exist')

    def get(self, request, format=None):
        contactus = ContactUs.objects.all()
        serializer = ContactUsSerializer(contuctus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        # Create a new con object
        contactus = ContactUs.objects.create(
            title=data['title'],
            sub_title=data['sub_title'],
            description=data['description'],
            logo=data['logo'],
        )

        # Save the con object
        contactus.save()

        # Return the con object
        return Response(contactus.data)


class Contact_Form_Api(APIView):

    def get(self, request, format=None):
        contactform = ContactForm.objects.all()
        serializer = ContactFormSerializer(contuctform, many=True)
        return Response(serializer.data)


"""
    def put(self, request, id):
        contuctus = ContuctUs.objects.all()

        contuctus.title = request.data['title']
        contuctus.sub_title = request.data['sub_title']
        contuctus.description = request.data['description']
        contuctus.logo = request.data['logo']

        contuctus.save()
        serializer = ContuctUsSerializer(contuctus, many=False)
        return Response(serializer.data)

        """
