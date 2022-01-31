from tkinter import CASCADE
from django.db import models

class GameCategory(models.Model):
    game = models.ForeignKey("Game", on_delete=CASCADE)
    category = models.ForeignKey("Category", on_delete=CASCADE)
    