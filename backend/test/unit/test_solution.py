import pytest
from src.controllers.recipecontroller import RecipeController
from unittest.mock import patch, MagicMock
import random
# different systems under test


# add your test case implementation here
@pytest.mark.unit
@pytest.fixture
def rc_controller():
    dao = MagicMock()
    return RecipeController(dao)


def test_no_recipes(rc_controller):
    mock_recipes = {
    }
    #mocking get_readiness_of_recipes return
    with patch.object(rc_controller, "get_readiness_of_recipes") as readiness_of_recipes:
        readiness_of_recipes.return_value = mock_recipes
        recipe = rc_controller.get_recipe(False, {})
        assert recipe == None

def test_readiness_under_01(rc_controller):
    mock_recipes = {
        "Recipe2": 0.09
    }
    #mocking get_readiness_of_recipes return
    with patch.object(rc_controller, "get_readiness_of_recipes") as readiness_of_recipes:
        readiness_of_recipes.return_value = mock_recipes
        recipe = rc_controller.get_recipe(False, {})
        assert recipe == None

def test_return_random(rc_controller):
    mock_recipes = {
        "Recipe1": 0.3,
        "Recipe2": 0.2
    }
    #mocking get_readiness_of_recipes return
    with patch.object(rc_controller, "get_readiness_of_recipes") as readiness_of_recipes:
        readiness_of_recipes.return_value = mock_recipes
        #mocking randint return
        with patch.object(random, "randint") as randint:
            randint.return_value = 1
            #I cant tell how the Diet dictionary should look like, but it doesnt matter since recipes come from get_readiness_of_recipes
            recipe = rc_controller.get_recipe(False, {})
            assert(recipe == "Recipe2")


def test_return_highest(rc_controller):
    mock_recipes = {
        "Recipe1": 0.3,
        "Recipe2": 0.2
    }
    #mocking get_readiness_of_recipes return
    with patch.object(rc_controller, "get_readiness_of_recipes") as readiness_of_recipes:
        readiness_of_recipes.return_value = mock_recipes
        #mocking randint return
        recipe = rc_controller.get_recipe(True, {})
        assert(recipe == "Recipe1")