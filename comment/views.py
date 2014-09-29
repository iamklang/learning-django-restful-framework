from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework import generics


class Comments(generics.ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    """
    curl http://localhost:9999/v1/comments/
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentDetail(generics.RetrieveAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    """
    curl http://localhost:9999/v1/comments/1/
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)