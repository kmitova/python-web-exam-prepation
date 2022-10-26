from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_NAME_LEN = 30
    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )


class Book(models.Model):
    MAX_LEN = 30
    title = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )
