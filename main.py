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

# Клиентский код
dough = Dough()
toppings = Toppings()
oven = Oven()
packaging = Packaging()

dough.prepare()
toppings.add()
oven.bake()
packaging.pack()