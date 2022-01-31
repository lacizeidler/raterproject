from tkinter import CASCADE
from django.db import models

class Review(models.Model):
    player = models.ForeignKey("Player", on_delete=CASCADE)
    game = models.ForeignKey("Game", on_delete=CASCADE)
    review = models.CharField(max_length=200)
    