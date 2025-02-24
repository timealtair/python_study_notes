
class Wallet:
    def __init__(self, start_amount):
        self._amount = start_amount

    def chech_amount(self):
        return self._amount

    def add_money(self, add_amount):
        self._amount = self._amount + add_amount

    def take_money(self, take_amount):
        self._amount = self._amount - take_amount
        return take_amount


if __name__ == '__main__':
    my_wallet = Wallet(0)
    print('Initial balance:')
    print(my_wallet.chech_amount())
    my_wallet.add_money(100)
    print('Current balance after adding 100:')
    print(my_wallet.chech_amount())
    print('Taked money:')
    print(my_wallet.take_money(40))
    print('Current balance:')
    print(my_wallet.chech_amount())
