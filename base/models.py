from django.db import models

# Create your models here.


class House(models.Model):
    des = models.JSONField()

class ways(models.Model):
    way = models.JSONField()
