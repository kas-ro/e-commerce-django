from django.db import models

class Collection(models.Model):
    title = models.CharField(
        verbose_name='titre',
        max_length=255,
    )
    description = models.CharField(
        verbose_name='description',
        max_length=255,
    )
    button_text = models.CharField(
        verbose_name='texte du button',
        max_length=255,
    )
    button_link = models.CharField(
        verbose_name='lien du boutton',
        max_length=255,
    )
    image = models.ImageField(
        verbose_name='images',
        upload_to='collections/%Y/%m/%d/'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date d'ajout",
    )
    updated_at = models.DateTimeField(
        verbose_name="date de mise à jours",
        auto_now=True,
    )