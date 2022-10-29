from django.core import exceptions
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def username_contains_validator(value):
    for ch in value:
        if not value.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore."
)


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            MinLengthValidator(MIN_USERNAME_LEN),
            username_contains_validator,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    GENRE_CHOICES = (
            (POP_MUSIC, POP_MUSIC),
            (JAZZ_MUSIC, JAZZ_MUSIC),
            (RNB_MUSIC, RNB_MUSIC),
            (ROCK_MUSIC, ROCK_MUSIC),
            (COUNTRY_MUSIC, COUNTRY_MUSIC),
            (DANCE_MUSIC, DANCE_MUSIC),
            (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
            (OTHER_MUSIC, OTHER_MUSIC),
        )
    MAX_LEN = 30

    album_name = models.CharField(
        max_length=MAX_LEN,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN,
        choices=GENRE_CHOICES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        ),
        null=False,
        blank=False,
    )

