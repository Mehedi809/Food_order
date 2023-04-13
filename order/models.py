from django.db import models

# Create your models here.

class custommer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    


    def __str__(self):
        return self.name
    

class product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    category = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    

class order(models.Model):
    status = (
        ('Pending', 'Pending'),
        ('Deliverd', 'Deliverd'),
        ('Out of delivery', 'Out of delivery')
    )
    custommer_id = models.ForeignKey(custommer, null=True, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(product, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=status)

    def __str__(self):
        return self.custommer_id.name