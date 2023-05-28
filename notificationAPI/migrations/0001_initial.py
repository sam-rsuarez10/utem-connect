# Generated by Django 4.2.1 on 2023-05-28 05:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('notification_type', models.CharField(choices=[('1', 'New Message'), ('2', 'New Request'), ('3', 'New Like')], max_length=20)),
            ],
        ),
    ]
