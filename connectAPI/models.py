from django.db import models
from userAPI.models import UtemUser
import uuid

# Create your models here.

class ConnectionRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    send_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user_from = models.ForeignKey(UtemUser, on_delete=models.CASCADE, related_name='sender')
    user_to = models.ForeignKey(UtemUser, on_delete=models.CASCADE, related_name='receiver')

class Connection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_a = models.ForeignKey(UtemUser, on_delete=models.CASCADE, related_name='user_a')
    user_b = models.ForeignKey(UtemUser, on_delete=models.CASCADE, related_name='user_b')

