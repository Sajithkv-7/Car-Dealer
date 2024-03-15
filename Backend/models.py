from django.db import models

# Create your models here.
class CarDb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Model = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Image_1 = models.ImageField(upload_to="Car-Images",null=True,blank=True)
    Image_2 = models.ImageField(upload_to="Car-Images", null=True, blank=True)
    Image_3 = models.ImageField(upload_to="Car-Images", null=True, blank=True)
    Image_4 = models.ImageField(upload_to="Car-Images", null=True, blank=True)
    Body_Style = models.CharField(max_length=50,null=True,blank=True)
    Features = models.CharField(max_length=200,null=True,blank=True)
    Price = models.CharField(max_length=50,null=True,blank=True)
    Mileage = models.CharField(max_length=50,null=True,blank=True)
    Engine = models.CharField(max_length=50,null=True,blank=True)
    Transmission = models.CharField(max_length=50,null=True,blank=True)
    Fuel_Type = models.CharField(max_length=50,null=True,blank=True)
    Seats = models.IntegerField(null=True,blank=True)
    Color = models.CharField(max_length=50,null=True,blank=True)
    Doors = models.IntegerField(null=True,blank=True)
    Year = models.IntegerField(null=True,blank=True)
    Type = models.CharField(max_length=50,null=True,blank=True)
    Power = models.CharField(max_length=50,null=True,blank=True)