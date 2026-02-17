from unittest import TestCase
from Dish import *

class TestDish(TestCase):
    def setUp(self):
        self.dish=Dish()
        self.dish_with_ing = Dish(["fries","tomato"])


    def test_add_ingredient(self):
        self.dish.add_ingredient("fries")
        self.assertEqual(self.dish.ingredients, ["fries"])

        self.dish.add_ingredient("tomato")
        self.assertEqual(self.dish.ingredients, ["fries","tomato"])

    def test_repr(self):
        self.assertEqual(repr(self.dish_with_ing), "* fries, tomato *")


    def test_eq(self):
        self.assertFalse(self.dish==self.dish_with_ing)
        dish1= Dish(["fries","tomato", "fries"])
        dish2 = Dish(["fries", "tomato"])
        dish3 = Dish(["fries", "fries", "tomato"])
        self.assertFalse(dish2==dish1)
        self.assertTrue(dish3 == dish1)
