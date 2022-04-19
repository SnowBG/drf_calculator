from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.


class User(models.Model):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(verbose_name='username', max_length=200)
    email = models.EmailField(verbose_name='email', unique=True)
