from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Roles definidos
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_representative = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=False)

    # Información adicional para todos los usuarios
    bio = models.TextField(blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
