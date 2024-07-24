from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(
        verbose_name='titre',
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='slug',
        max_length=255,
    )
    description = models.CharField(
        verbose_name='description',
        max_length=255,
    )
    more_description = models.TextField(
        verbose_name='plus de descriptions',
        blank=True,
    )
    additional_infos = models.TextField(
        verbose_name='description additionelles',
        blank=True,
    )
    stock = models.IntegerField(
        verbose_name="stock",
    )
    solde_price = models.IntegerField(
        verbose_name="prix promotionnel",
    )
    regular_price = models.IntegerField(
        verbose_name="prix régulier",
    )
    brand = models.CharField(
        verbose_name="brand",
        max_length=255,
    )
    is_availlable = models.BooleanField(
        verbose_name='est disponible ?',
        default=True,
    )
    is_best_seller = models.BooleanField(
        verbose_name='est best seller ?',
        default=True,
    )
    is_new_arrival = models.BooleanField(
        verbose_name='nouvelle arrivage ?',
        default=True,
    )
    is_featured = models.BooleanField(
        verbose_name='en vedette ?',
        default=True,
    )
    is_specail_offer = models.BooleanField(
        verbose_name='offre spéciale ?',
        default=True,
    )
    is_mega = models.BooleanField(
        verbose_name='est méga ?',
        default=False,
    )
    categories = models.ManyToManyField(
        to='shop.Category',
        blank=True,
        null=True,
        related_name='product_category_set',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date d'ajout",
    )
    updated_at = models.DateTimeField(
        verbose_name="date de mise à jours",
        auto_now=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)