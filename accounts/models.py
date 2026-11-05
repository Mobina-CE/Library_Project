from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_librarian = models.BooleanField(default = False, verbose_name ="Is Librarian?")

    def __str__(self):
        return self.username


