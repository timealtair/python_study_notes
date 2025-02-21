
class Wallet:
    def __init__(self, start_amount):
        self._amount = start_amount

    def get_amount(self):
        return self._amount

    def add_money(self, add_amount):
        self._amount = self._amount + add_amount

    def take_money(self, take_amount):
        self._amount = self._amount - take_amount
        return take_amount
