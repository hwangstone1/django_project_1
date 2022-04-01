from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment')

    content = models.TextField(max_length=200, null=False)
    created_at = models.DateField(auto_now=True)