from django.db import models

class ImageProduct(models.Model):
    image = models.ImageField(
        verbose_name="image du produit",
        upload_to="products/images/%Y/%m/%d/"
    )
    product = models.ForeignKey(
        to='shop.Product',
        verbose_name='image du produit',
        on_delete=models.CASCADE,
        related_name='images',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date d'ajout",
    )
    updated_at = models.DateTimeField(
        verbose_name="date de mise à jours",
        auto_now=True,
    )