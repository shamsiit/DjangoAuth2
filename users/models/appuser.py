import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    uuid = models.CharField(max_length=64, verbose_name=u"uuid", default=uuid.uuid1)