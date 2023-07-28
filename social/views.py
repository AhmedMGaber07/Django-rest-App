from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Social
from .serializers import SocialSerializer

# Create your views here.


@api_view(['GET'])
def social_list(request):
    query = request.GET.get('query')
    if query == None:
        query = ''

    social = Social.objects.filter(
        Q(id__icontains=query))
    serializer = SocialSerializer(social, many=True)
    return Response(serializer.data)


class SocialDetails(APIView):

    def get_object(self, id):
        try:
            return Social.objects.get(id=id)
        except Social.DoesNotExist:
            raise Response('Social Does Not Exist')

    def get(self, request, id):
        social = self.get_object(id)
        serializer = SocialSerializer(social, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        social = self.get_object(id)
        # social.facebooksvg = request.data['facebooksvg']
        # social.facebookurl = request.data['facebookurl']
        social.save()
        serializer = SocialSerializer(social, many=False)
        return Response(serializer.data)
