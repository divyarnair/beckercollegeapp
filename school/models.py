
from django.db import models
from django import forms


# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=250,null=True)
    password=models.CharField(max_length=250,null=True)

    def __str__(self):
       return self.username


class Customer(models.Model):
    name=models.CharField(max_length=250)
    birthDate=models.DateField()
    Age=models.IntegerField(null=0)
    gender=models.CharField(max_length=250)
    phoneNumber=models.IntegerField()
    Email=models.EmailField(max_length=250,primary_key=True)
    address=models.TextField(max_length=250)


    def __str__(self):
        return self.Email




