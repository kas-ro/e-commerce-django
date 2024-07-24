from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(
        verbose_name='titre',
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='description',
        max_length=255,
    )
    description = models.CharField(
        verbose_name='description',
        max_length=255,
    )
    image = models.ImageField(
        verbose_name='images',
        upload_to='categories/%Y/%m/%d/'
    )
    is_mega = models.BooleanField(
        verbose_name='est méga ?',
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date d'ajout",
    )
    updated_at = models.DateTimeField(
        verbose_name="date de mise à jours",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)