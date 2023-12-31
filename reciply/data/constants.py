# Standard library imports
import enum

# Django imports
from django.db import models as django_models


class MediaNamespace(enum.StrEnum):
    """
    Namespace for accessing certain types of media files in storage.
    """

    RECIPES = "recipes"


class Day(django_models.IntegerChoices):
    MONDAY = 1, "Monday"
    TUESDAY = 2, "Tuesday"
    WEDNESDAY = 3, "Wednesday"
    THURSDAY = 4, "Thursday"
    FRIDAY = 5, "Friday"
    SATURDAY = 6, "Saturday"
    SUNDAY = 7, "Sunday"


class MealTime(django_models.TextChoices):
    BREAKFAST = "BREAKFAST", "Breakfast"
    LUNCH = "LUNCH", "Lunch"
    DINNER = "DINNER", "Dinner"
