from django.db import models

# Create your models here.

class daily(models.Model):
    title= models.CharField(max_length=120)
    sub_title= models.CharField(max_length=120)
    img = models.ImageField(upload_to='')
    desc = models.TextField()
