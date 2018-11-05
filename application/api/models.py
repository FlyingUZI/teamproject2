from django.db import models

# Create your models here.


class Info(models.Model):
    user_id = models.CharField(max_length=100)
    user_pass = models.CharField(max_length=100)
    room = models.CharField(max_length=100)