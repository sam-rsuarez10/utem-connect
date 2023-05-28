from django.db import models
from userAPI.models import UtemUser
import uuid

# Create your models here.

# class representing a class between two users
class Chat (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_1 = models.ForeignKey(UtemUser, on_delete=models.CASCADE, related_name="user_1")
    user_2 = models.ForeignKey(UtemUser, on_delete=models.CASCADE, related_name="user_2")

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    send_date = models.DateField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class GroupChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now_add=True)

class GroupMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    send_date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE)

# model that stores the information about the groups' participants
class UserGroup(models.Model):
    group= models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    user = models.ForeignKey(UtemUser, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['group', 'user'], name='user_group_pk')
        ]