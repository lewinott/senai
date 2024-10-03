
from water import Water

class MotorBoat(Water):
    def __init__ (self, type_boat, capacity):
        self.__type_motorboat = type_boat
        self.__capacity = capacity

    
    def start_engine(self):
        if self.__type_motorboat = "Motor"
            print("Motor ligado!")
        else:
            print("Motor desligado!")
