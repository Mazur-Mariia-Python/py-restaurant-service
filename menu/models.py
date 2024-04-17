from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    dish_type_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("dish_type_name",)

    def __str__(self):
        return self.dish_type_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("ingredient_name",)

    def __str__(self):
        return self.ingredient_name


class Specialization(models.Model):
    specialization_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("specialization_name",)

    def __str__(self):
        return self.specialization_name


class Cook(AbstractUser):

    years_of_experience = models.IntegerField(blank=True)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name="cooks",
        blank=True,
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    dish_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )

    class Meta:
        ordering = ("dish_name",)
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.dish_name
