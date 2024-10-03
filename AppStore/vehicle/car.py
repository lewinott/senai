from land import Land

class Car(Land):
    def __init__(self, gear, conditioning_air):
        self.__gear = gear
        self.__conditioning_air = conditioning_air

    def get_gear(self):
        return self.__gear
    
    def set_gear(self, gear)
        self.__gear = gear
    
    def turn_on_conditioning(self):
        if self.__conditioning_air == True:
            print("Ar condicionado ligado!")
        else:
            print("Ar condicionado desligado!")