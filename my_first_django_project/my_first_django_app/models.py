from django.db import models

img = models.ImageField(upload_to='images')


# Create your models here.
class Portfolio(models.Model):
    name=models.CharField(max_length = 250)
    description=models.TextField()

    def __str__(self):
        return self.name

class Teams(models.Model):
    team_name=models.CharField(max_length = 250)
    img = models.ImageField(upload_to='Imagesss')
    description=models.TextField()

    def __str__(self):
        return self.team_name
