import logging
from django.contrib.auth.models import AbstractUser
from django.db import models

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):


    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            logger.info(f"New user created: {self.username} (ID: {self.pk})")
        else:
            logger.info(f"User updated: {self.username} (ID: {self.pk})")

    def __str__(self):
        return self.username
