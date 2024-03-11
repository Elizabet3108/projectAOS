class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, ${self.price}, count: {self.quantity}"

    def __repr__(self):
        return f"Product: {self.name}, ${self.price}, count: {self.quantity}"

