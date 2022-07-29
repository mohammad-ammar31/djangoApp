from django.db import models

# Create your models here.


class Food(models.Model):
    foodName = models.CharField(max_length=100, null=False)
    foodType = models.CharField(max_length=100)
    pinCode = models.IntegerField(default=0)