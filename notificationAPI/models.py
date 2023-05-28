from django.db import models
from userAPI.models import UtemUser
import uuid
# Create your models here.

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_to = models.ForeignKey(UtemUser, on_delete=models.CASCADE)
    
    NOTIFICATION_TYPES = (
        ('1', 'New Message'),
        ('2', 'New Request'),
        ('3', 'New Like'),
    )
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)