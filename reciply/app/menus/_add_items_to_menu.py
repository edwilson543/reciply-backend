# Standard library imports
from typing import TypedDict

# Django imports
from django import db as django_db

# Local application imports
from data import constants
from data.menus import models as menu_models
from data.recipes import models as recipe_models


class MealTimesAreNotUnique(django_db.IntegrityError):
    pass


class InvalidRecipeIds(django_db.IntegrityError):
    pass


class MenuItem(TypedDict):
    recipe_id: int
    day: constants.Day
    meal_time: constants.MealTime


def add_items_to_menu(
    *, menu: menu_models.Menu, items: list[MenuItem]
) -> list[menu_models.MenuItem]:
    recipe_ids = [item.get("recipe_id") for item in items]
    if recipe_models.Recipe.objects.filter(id__in=recipe_ids).count() < len(items):
        raise InvalidRecipeIds

    menu_items = [
        menu_models.MenuItem(
            menu=menu,
            recipe_id=item["recipe_id"],
            meal_time=item["meal_time"],
            day=item["day"],
        )
        for item in items
    ]

    try:
        return menu.add_items(items=menu_items)
    except django_db.IntegrityError:
        raise MealTimesAreNotUnique
