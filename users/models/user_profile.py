import uuid

from django.db import models

from .appuser import AppUser

class UserProfile(models.Model):
    uuid = models.CharField(max_length=64, verbose_name=u"uuid", default=uuid.uuid1, blank=True, null=True)
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    age = models.IntegerField()