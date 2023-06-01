from django.db import models

# Create your models here.
"""
Produit
-nom
-prix
-stock
-description
-image
"""


class Product(models.Model):
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    prix = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.stock})"
