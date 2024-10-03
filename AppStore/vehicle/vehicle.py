from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel, color, brand, current_speed, acceleration, max_speed):
        self._fuel = fuel
        self._color = color
        self._brand = brand
        self._current_speed = current_speed
        self._acceleration = acceleration
        self._max_speed = max_speed

    
    @abstractmethod
    def accelerating(self):
        if self._current_speed < self._max_speed:
            self._current_speed += self._acceleration
            print(f"Esse veículo está a {self._current_speed} KM/h")
        else:
            print("O veículo está na velocidade máxima")

    @abstractmethod
    def decelerate(self):
        if self._current_speed > 0:
            self._current_speed -= self._acceleration
            print(f"O veículo está a {self._current_speed} KM/h")
        else:
            print("O veículo está parado")

    def get_fuel(self):
        return self._fuel
    def get_color(self):
        return self._color
    def get_brand(self):
        return self._brand
    def get_current_speed(self):
        return self._current_speed
    def get_acceleration(self):
        return self._acceleration
    def get_max_speed(self):
        return self._max_speed

    def set_fuel(self, fuel):
        self._fuel = fuel
    def set_color(self, color):
        self._color = color
    def set_brand(self, brand):
        self._brand = brand
    def set_acceleration(self, acceleration):
        self._acceleration = acceleration
    def set_max_speed(self, max_speed):
        self._max_speed = max_speed
