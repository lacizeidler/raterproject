from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=50)
