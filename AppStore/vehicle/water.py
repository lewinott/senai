from vehicle import Vehicle

class Water(Vehicle):
    def __init__(self, deep):
        self.deep = deep
    
        
    @abstractmethod
    def accelerating(self):
        if self._current_speed < self._max_speed:
            self._current_speed += self._acceleration
            print(f"Esse veículo está a {self._current_speed} Kn")
        else:
            print("O veículo está na velocidade máxima")

    @abstractmethod
    def decelerate(self):
        if self._current_speed > 0:
            self._current_speed -= self._acceleration
            print(f"O veículo está a {self._current_speed} Kn")
        else:
            print("O veículo está parado")
