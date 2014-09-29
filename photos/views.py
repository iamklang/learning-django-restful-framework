from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.response import Response
from photos.models import Photos
from photos.serializers import PhotoSerializer


class PhotoViewSet(generics.ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PhotoViewList(generics.RetrieveAPIView):

    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
