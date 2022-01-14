from django.db import models


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Catagories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name


class Accessory(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    vehicle_make = models.CharField(max_length=50, null=False, blank=False)
    vehicle_model = models.CharField(max_length=50, null=False, blank=False)
    brand = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    quantity_available = models.IntegerField(null=False, blank=False)
    accessory_type = models.CharField(max_length=254, null=False, blank=False)
    type = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
