from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import News, NewsTitle


class NewsSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'image']


class NewsTitleSerializer(ModelSerializer):

    class Meta:
        model = NewsTitle
        fields = ['paragraph', 'order', 'list_items']
