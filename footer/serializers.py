from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Certificate


class CertificateSerializer(ModelSerializer):

    class Meta:
        model = Certificate
        fields = ['certificate', 'pdf']
