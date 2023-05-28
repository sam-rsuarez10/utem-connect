from django.db import models
from userAPI.models import UtemUser
import uuid

# Create your models here.

class LearningLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(UtemUser, on_delete=models.CASCADE)

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(UtemUser, on_delete=models.CASCADE)
    learning_log = models.ForeignKey(LearningLog, on_delete=models.CASCADE)

class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    record_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(UtemUser, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


