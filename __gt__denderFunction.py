class order:
    def __init__(self, item ,price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price == order2.price

order1 = ("veg",25)
order2 = ("non-veg",30)

print(order1 < order2)  #agar hoga to print true krega