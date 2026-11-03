from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length = 50, verbose_name="Username" )
    email = models.CharField(max_length = 50, verbose_name="Email Address")
    password = models.CharField(max_length = 50, verbose_name="Password")
    is_librarian = models.BooleanField(default = False, verbose_name ="Is Librarian?")

    def __str__(self):
        return self.username


