from django.db import models
from decimal import Decimal


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "Hardcover"
        SOFT = "Softcover"

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=15, choices=CoverChoices.choices, default=CoverChoices.HARD
    )
    inventory = models.PositiveIntegerField(
        default=0, help_text="Number of copies available in the book_service."
    )
    daily_fee = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )

    def __str__(self):
        return f"{self.title}-{self.author} ({self.inventory} pcs)"

    class Meta:
        ordering = ["title"]
