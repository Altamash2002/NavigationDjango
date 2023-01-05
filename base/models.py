from django.db import models

# Create your models here.


class House(models.Model):
    des = models.TextField()

class ways(models.Model):
    way = models.TextField()
