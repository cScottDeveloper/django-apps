from django.db import models

# Create your models here.


# You do not have to specify an ID, it is given by the Database
# to convert a class as a model use this parameter
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    desc = models.TextField()
    offer = models.BooleanField(default=False)

