from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class UtemUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    middle_name  = models.CharField(max_length=50, blank=True, null=True)
    second_surname = models.CharField(max_length=50, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Student(models.Model):
    user = models.OneToOneField(UtemUser, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_photo = models.BinaryField(blank=True, null=True)
    career = models.CharField(max_length=50)
    personal_description = models.TextField()
    connections = models.IntegerField()
