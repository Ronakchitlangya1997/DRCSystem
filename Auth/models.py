from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class DRCUser(AbstractUser):
  Phone_number = models.CharField(max_length = 10, unique=True)
  def __str__(self):
      return self.username 