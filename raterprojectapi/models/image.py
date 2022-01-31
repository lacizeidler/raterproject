from tkinter import CASCADE
from django.db import models

class Image(models.Model):
    player = models.ForeignKey("Player", on_delete=CASCADE)
    game = models.ForeignKey("Game", on_delete=CASCADE)
    picture = models.ImageField()