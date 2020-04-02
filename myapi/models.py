from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Villain(models.Model):
    hero = models.ForeignKey(Hero, related_name='villains', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    super_power = models.CharField(max_length=100)

    def __str__(self):
        return self.name
