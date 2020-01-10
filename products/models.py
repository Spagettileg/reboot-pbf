from django.db import models

category_choices = (
    ('All','All'),
    ('Juniors','Juniors'),
    ('Adults','Adults'),
)

class Product(models.Model):
    make = models.CharField(max_length=254, default='')
    """ No default product will be added into the database """
    category = models.CharField(max_length=254, choices=category_choices, default='')
    """ Category choices include view all, juniors and adults """
    size = models.IntegerField()
    """ Size of the product """
    colour = models.TextField()
    """ Product colour """
    studs = models.TextField()
    """ Stud configuration of boot. Either moulded or screwin """
    quality = models.TextField(null=True)
    """ Brand new, almost new and general wear """ 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    """ Pricing model will be less than £1m and decimal places = pence """
    image = models.ImageField(upload_to='images')
    """ Allow images to be uploaded for our products """
    
    def __str__(self):
        return self.name  # A string will be returned with the name
        
        

    

