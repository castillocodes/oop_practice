class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 7)

item2 = Item("Laptop", 1000, 3)

print(f"An instance created: {item1.name}, {item1.quantity} at ${item1.price} each = ${item1.calculate_total_price()}.")
print(f"An instance created: {item2.name}, {item2.quantity} at ${item2.price} each = ${item2.calculate_total_price()}.")
