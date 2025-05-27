from django.db import models
# Bino ma'lumotlari modeli
class Hotel(models.Model):


    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    roooms = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    star = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Famous_Hotels(models.Model):


    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    descreption1 = models.CharField(max_length=100)
    descreption2 = models.CharField(max_length=100)
    descreption3 = models.CharField(max_length=100)


    def __str__(self):
        return self.descreption1