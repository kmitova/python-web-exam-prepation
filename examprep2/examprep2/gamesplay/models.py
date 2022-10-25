from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12
    MAX_PASS_LEN = 30
    MAX_FN_LEN = 30
    MAX_LN_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FN_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LN_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    CATEGORY_CHOICES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    MAX_LEN_TITLE = 30
    MAX_CAT_LEN = 15
    MAX_RATING = 5.0
    MIN_RATING = 1.0

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_CAT_LEN,
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING),
        ),
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
