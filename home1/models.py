from django.db import models

# Create your models here.


class about(models.Model):
  name = models.CharField(max_length=30)
  designation = models.CharField(max_length=30)
  image=models.ImageField(upload_to='static/about', default='')
  description = models.TextField()
  email  = models.EmailField(max_length=70,blank=True,unique=True)



class iceCream(models.Model):
   flavour = models.CharField(max_length=30)
   size = models.CharField(max_length=30)
   price=models.CharField(max_length=30)
   offer_price = models.CharField(max_length=30)
   icecream_photo = models.ImageField(upload_to='static/icecream', default='')
   description = models.TextField()

class carousel(models.Model):
  name = models.CharField(max_length=30)
  image = models.ImageField(upload_to='static/carousel', default='')
  description = models.TextField()


class Contact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    subject = models.TextField()
    def __str__(self):
       return self.fname