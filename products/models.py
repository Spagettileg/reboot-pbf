from django.db import models

category_choices = (
    ('Juniors', 'Juniors'),
    ('Adults', 'Adults'),
)

quality_choices = (
    ('Brand New', 'Brand New'),
    ('Almost New', 'Almost New'),
    ('Used Boots', 'Used Boots'),
)

stud_choices = (
    ('Screw in', 'Screw in'),
    ('Moulded', 'Moulded'),
)


class Product(models.Model):
    make = models.CharField(max_length=254)
    """ No default product will be added into the database """
    category = models.CharField(max_length=254, choices=category_choices)
    """ Category choices include view all, juniors and adults """
    customer = models.CharField(max_length=50, choices=category_choices,
                                null=True)
    """ Junior rugby players """
    size = models.IntegerField()
    """ Size of the product """
    colour = models.CharField(max_length=50)
    """ Product colour """
    studs = models.CharField(max_length=50, choices=stud_choices)
    """ Stud configuration of boot. Either moulded or screwin """
    quality = models.CharField(max_length=50, choices=quality_choices,
                               null=True)
    """ Brand new, almost new and general wear """
    price = models.DecimalField(max_digits=6, decimal_places=2)
    """ Pricing model will be less than £1m and decimal places = pence """
    image = models.ImageField(upload_to='images', blank=True, null=True)
    """ Allow images to be uploaded for our products """

    def __str__(self):
        return self.make  # String will be returned with the make of rugby boot
