from django.db import models

# Create your models here.
class Sign_up(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
   
class Contact_data(models.Model):
    message = models.CharField(max_length=500)
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)   

class Subscribe(models.Model):
    e_mail = models.CharField(max_length=50)
    
class Application(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    CV = models.FileField(upload_to="Application/",max_length=250,null=True,default=None)
    coverletter = models.CharField(max_length=1000)
    