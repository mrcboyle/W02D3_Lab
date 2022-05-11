import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Guinness", 5.00, 2)

    def test_drink_has_name(self):
        self.assertEqual("Guinness", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)

    def test_has_alcohol_level(self):
        self.assertEqual(2, self.drink._alcohol_level)