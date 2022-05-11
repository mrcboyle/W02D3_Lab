
class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def decrease_wallet(self, drink_price):
        self.wallet -= drink_price

    def buy_drink(self, pub, drink):
        self.decrease_wallet(drink.price)
        pub.increase_till(drink.price)