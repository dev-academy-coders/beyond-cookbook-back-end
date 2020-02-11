from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    about = models.TextField(max_length=512, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
