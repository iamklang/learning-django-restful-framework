from rest_framework import generics
from django.contrib.auth.models import User
from myassignment.serializers import UserSerializer


class UserViewSet(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class UserViewList(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)