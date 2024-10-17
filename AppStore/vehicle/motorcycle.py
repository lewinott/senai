from land import Land

class Motorcycle(Land):
    def __init__(self, trunk_capacity):
        self.__trunk_capacity = trunk_capacity

    def fill_trunk(self):
        if self.__trunk_capacity = "fill"
            print ("Capacidade cheia...")
        else:
            print("Espaço disponível")