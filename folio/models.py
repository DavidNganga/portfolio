from django.db import models

# Create your models here.
class Project(models.Model):
     name = models.CharField(max_length=20)
     link_url = models.TextField(blank = True)
     description = models.CharField(max_length=200)
     screenshot = models.ImageField(upload_to ='images/',null = True )
