from django.db import models

# Create your models here.
class menuItem(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    
    
class resverations(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    guest_count=models.IntegerField(default=1)
    resverations_time=models.DateField(auto_now=True)
    comments=models.CharField(max_length=1000)
    
    
    