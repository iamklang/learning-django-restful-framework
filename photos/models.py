from django.db import models
from django.contrib.auth.models import User
import json

class Photos(models.Model):
    user = models.ForeignKey(User)
    url = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)

    def get_comment(self):
        all_comment = {}
        comments = self.comment_set.all()
        for comment in comments:
            all_comment[comment.id] = comment.comment

        return all_comment