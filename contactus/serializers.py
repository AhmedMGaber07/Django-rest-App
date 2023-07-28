from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import ContactUs, ContactForm


class ContactUsSerializer(ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ['title', 'sub_title', 'description', 'logo']


class ContactFormSerializer(ModelSerializer):

    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']
