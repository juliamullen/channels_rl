from django.db import models
from django.contrib.auth.models import User

class Entity(models.Model):
    x    = models.PositiveIntegerField()
    y    = models.PositiveIntegerField()
    name = models.CharField(max_length=20)


class Character(Entity):
    user = models.ForeignKey(User)
    pass
