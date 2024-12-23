class Dough:
    def prepare(self):
        print("Preparing dough")

class Toppings:
    def add(self):
        print("Adding toppings")

class Oven:
    def bake(self):
        print("Baking pizza")

class Packaging:
    def pack(self):
        print("Packing pizza")

class PizzaFacade:
    def __init__(self):
        self.dough = Dough()
        self.toppings = Toppings()
        self.oven = Oven()
        self.packaging = Packaging()

    def order_pizza(self):
        self.dough.prepare()
        self.toppings.add()
        self.oven.bake()
        self.packaging.pack()

# Клиентский код
pizza_facade = PizzaFacade()
pizza_facade.order_pizza()
