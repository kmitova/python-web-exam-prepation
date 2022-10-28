from django.db import models


class Recipe(models.Model):
    MAX_LEN_TITLE = 30
    MAX_ING_LEN = 250
    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    ingredients = models.CharField(
        max_length=MAX_ING_LEN,
        null=False,
        blank=False,
    )

    time = models.IntegerField(
        null=False,
        blank=False,
    )
