from django.db import models

# Create your models here.

#book table model
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    people = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
# #sigup model
# class User(models.Model):
#     fullname = models.CharField(max_length=100)
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     password = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
#     # Add any other fields you need

#     def __str__(self):
#         return self.username

#inbuilt user for authentication
from django.contrib.auth.models import User

class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username



    




    










    

