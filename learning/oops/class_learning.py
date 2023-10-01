#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

class Item:
    def __init__(self):
        print("I am created!")

    @staticmethod
    def calc_total_price(price, quantity):
        return price * quantity


item1 = Item()
item1.type = "Mobile"
item1.price = 2410
item1.count = 5
print(item1.calc_total_price(item1.price, item1.count))

item2 = Item()
item2.type = "Laptop"
item2.price = 35235
item2.count = 2
print(item2.calc_total_price(item2.price, item2.count))

print("\n")


class ItemConst:
    pay_rate = 0.8  # after discounting 20% on the product price

    def __init__(self, product: str, price: int, quantity=0):
        assert price > 0, f"Price {price} is not valid!"
        assert quantity > 0, f"Quantity {quantity} is not valid!"
        assert len(product) > 0, "write a valid Product Name"
        self.product = product
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        print(self.price)


product1 = ItemConst("Phone", 100, 9)
print(product1.calculate_total_price())

product2 = ItemConst("Laptop", 24532, 4)
print(product2.calculate_total_price())

product1.apply_discount()
product2.pay_rate = 0.7
product2.apply_discount()
print(ItemConst.__dict__)  # all the attribute of class level
print(product1.__dict__)  # all the attribute of intance level
