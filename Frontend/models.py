from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class RegistrationDb(models.Model):
    FirstName = models.CharField(max_length=50,null=True,blank=True)
    LastName = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Username = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)

class ContactDb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=200,null=True,blank=True)

class EnquiryDb(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=50,null=True,blank=True)
    Car_Name = models.CharField(max_length=50,null=True,blank=True)
    Offer = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Car_Id = models.IntegerField(null=True,blank=True)
    Price = models.CharField(max_length=50,null=True,blank=True)
    Status = models.IntegerField(default=0)

class Review(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Stars = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=200,null=True,blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    email_verified = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.Username

class PaymentDb(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    car_name = models.CharField(max_length=50, null=True, blank=True)
    car_id = models.IntegerField(null=True, blank=True)
    amount = models.CharField(max_length=50,null=True,blank=True)
    order_id = models.CharField(max_length=50, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    paid = models.BooleanField(default=False)

