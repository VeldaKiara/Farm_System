from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Fertilizer(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    

    def __str__(self):
        return self.name

class Pesticide(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    

    def __str__(self):
        return self.name

class Machinery(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    
    def __str__(self):
        return self.name

class Tools(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()

    def __str__(self):
        return self.name
