from django.db import models
from photos.models import Photos


class Comment(models.Model):
    photo = models.ForeignKey(Photos)
    comment = models.CharField(max_length=200)
