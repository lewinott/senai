from vehicle import Vehicle

class Land(Vehicle):
    def __init__ (self, wheel):
        self.amount_wheel = wheel

    def change_wheels(self):
        print("Trocando rodas...")
