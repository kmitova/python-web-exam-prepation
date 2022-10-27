from django.db import models


class Profile(models.Model):
    MAX_LEN_NAME = 20
    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )


class Note(models.Model):
    MAX_TITLE_LEN = 30
    title = models.CharField(
        max_length=MAX_TITLE_LEN,

    )

    image_url = models.URLField(

    )

    content = models.TextField(

    )