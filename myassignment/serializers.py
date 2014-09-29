from rest_framework import serializers
from django.contrib.auth.models import User
from photos.serializers import PhotoSerializer

class UserSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photo')
    serializer_class = PhotoSerializer

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'photos')
        
    def get_photo(self, obj):
        user = User.objects.get(username=obj)
        photos = user.photos_set.all()
        serializer = PhotoSerializer(photos, many=True)
        return serializer.data