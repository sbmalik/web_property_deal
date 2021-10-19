from django.db import models


# Create your models here.
class Home(models.Model):
    # this is our table/model for database
    # all the fields are selected according to requirements.
    name = models.CharField(max_length=122)
    rooms = models.IntegerField()
    bath = models.IntegerField()
    price = models.FloatField()
    pic = models.ImageField(upload_to='static/images/')
    garage = models.CharField(max_length=10)
    balcony = models.CharField(max_length=10, default='No')
    shared = models.CharField(max_length=10)
    bond = models.CharField(max_length=50)
    available = models.CharField(max_length=122)
    ow_email = models.EmailField()
    ow_phone = models.CharField(max_length=122)
    description = models.TextField()
    status = models.CharField(max_length=10, default='Awaiting')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    owners = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.price}'
