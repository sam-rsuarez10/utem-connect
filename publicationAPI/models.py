from django.db import models
from userAPI.models import UtemUser
import uuid

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField()
    publisher = models.ForeignKey(UtemUser, on_delete=models.CASCADE)

class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UtemUser, on_delete=models.CASCADE)