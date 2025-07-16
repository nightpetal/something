from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    price = models.FloatField(default=99.99)
    image_url = models.URLField(max_length=300, null=True)

    def __str__(self):
        return self.product_name

