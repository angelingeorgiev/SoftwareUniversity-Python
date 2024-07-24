class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        # decrease quantity only if there is enough
        if quantity <= self.quantity:
            self.quantity -= quantity

    def increase(self, quantity: int):
        # increase quantity of the product
        self.quantity += quantity

    def __repr__(self):
        return self.name
    