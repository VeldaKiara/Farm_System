from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    products_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Fertilizer(models.Model):
    name = models.CharField(max_length=150)
    fertilizer_id= models.CharField(max_length=100)
    Products_id = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Pesticide(models.Model):
    name = models.CharField(max_length=150)
    pesticide_id= models.CharField(max_length=100)
    fertilizer_id = models.ForeignKey(Fertilizer, on_delete=models.CASCADE, blank=, null=True)

    def __str__(self):
        return self.name

class Machinery(models.Model):
    name = models.CharField(max_length=150)
    machinery_id= models.CharField(max_length=100)
    pesticide_id = models.ForeignKey(Pesticide, on_delete=models.CASCADE, blank=, null=True)

    def __str__(self):
        return self.name

class Tools(models.Model):
    name = models.CharField(max_length=150)
    tools_id= models.CharField(max_length=100)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE, blank=, null=True)

    def __str__(self):
        return self.name
