import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Swan", 500.00)

    def test_pub_has_name(self):
        self.assertEqual("The Swan", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.pub.till)

    def test_increase_till(self):
        drink1 = Drink("Guinness", 5.00)
        self.pub.increase_till(drink1.price)
        self.assertEqual(505.00, self.pub.till) 