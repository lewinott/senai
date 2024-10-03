from vehicle import Vehicle

class Air(Vehicle):
    def __init__(self, max_height):
        self._max_height = max_height

    def fly(self):
        print("Voando!")