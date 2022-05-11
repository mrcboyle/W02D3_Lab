import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Idris", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("Idris", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_decrease_wallet(self):
        drink1 = Drink("Guinness", 5.00)
        self.customer.decrease_wallet(drink1.price)
        self.assertEqual(45.00, self.customer.wallet)

    def test_buy_drink(self):
        drink1 = Drink("Guinness", 5.00)
        pub1 = Pub("The Swan", 500.00)
        self.customer.buy_drink(pub1, drink1)
        self.assertEqual(45.00, self.customer.wallet)
        self.assertEqual(505.00, pub1.till)