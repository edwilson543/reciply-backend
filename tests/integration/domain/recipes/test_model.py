# Local application imports
from reciply.data import constants
from reciply.domain import recipes
from tests import factories


class TestRecipeFromOrmModel:
    def test_converts_recipe_orm_model_with_requirements_to_recipe_domain(self):
        meal_times = [constants.MealTime.LUNCH, constants.MealTime.DINNER]
        orm_recipe = factories.Recipe(meal_times=meal_times)

        # Make sure the recipe will have some nutritional information.
        ingredient = factories.Ingredient()
        factories.IngredientNutritionalInformation(ingredient=ingredient)
        factories.RecipeIngredient(recipe=orm_recipe, ingredient=ingredient)

        recipe = recipes.Recipe.from_orm_model(recipe=orm_recipe)

        assert recipe.id == orm_recipe.id
        assert recipe.meal_times == tuple(meal_times)
        assert len(recipe.nutritional_information) > 0