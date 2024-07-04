from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Photo(models.Model):
    
    image = models.ImageField(upload_to='uploads/photos')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description or str(self.id)  #recommendation describe your photos according to their purpose e.g car-wash-woman-washing-car
    
    
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2, default = 100)
    duration = models.PositiveIntegerField(default=2)
    photos = models.ManyToManyField(Photo, related_name='related_photos')

    #rating = models.PositiveIntegerField(default=5, MaxValueValidator = 5, MinValueValidator = 1)


    def __str__(self):
        return self.name

