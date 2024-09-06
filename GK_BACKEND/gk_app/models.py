from django.db import models

# Create your models here.

class registration(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=300,null=False)
    mobileNo = models.CharField(max_length=10)
    aadharNo = models.CharField(max_length=12, default='NULL')
    native = models.CharField(max_length=300,  default='NULL')
    password = models.CharField(max_length=300)
    roleId = models.IntegerField(null=False)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length = 255, null=True)
    userEmail = models.CharField(max_length = 255, null=True)
    userPhone=models.CharField(max_length = 255, null=True)
    
class OTP(models.Model):
    id = models.AutoField(primary_key=True)
    otp = models.CharField(max_length = 255, null=True)
    userId = models.CharField(max_length = 255, null=True)
    userPhone=models.CharField(max_length = 255, null=True)

