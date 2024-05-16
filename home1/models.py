from django.db import models

# Create your models here.


class about(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  subject = models.TextField()


class iceCream(models.Model):
   flavour = models.CharField(max_length=30)
   size = models.CharField(max_length=30)
   price=models.CharField(max_length=30)
   offer_price = models.CharField(max_length=30)
   icecream_photo = models.ImageField(max_length=200)
   description = models.TextField()
   
        