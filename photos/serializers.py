from rest_framework import serializers
from photos.models import Photos


class PhotoSerializer(serializers.ModelSerializer):
    comments = serializers.CharField(source='get_comment', read_only=True)

    class Meta:
        model = Photos
        fields = ('id', 'url', 'description', 'comments')
        