from django.db import models

# Create your models here.


class House(models.Model):
    des = models.JSONField()
    def __str__(self):
        return 'Haus' + str(self.id)
    

class ways(models.Model):
    way = models.JSONField()
    def __str__(self):
        return 'Way' + str(self.id)
    
