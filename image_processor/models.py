from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    input_url = models.URLField()
    output_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')

