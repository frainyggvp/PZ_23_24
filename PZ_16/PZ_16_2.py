"""Создание базового класса "Транспортное средство" и его наследование для создания
классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
общие свойства, такие как максимальная скорость и количество колес,
а классы наследники будут иметь свои уникальные свойства и методы."""


class Vehicle:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels


class Car(Vehicle):
    def __init__(self, max_speed, wheels, body):
        super().__init__(max_speed, wheels)
        self.body = body


class Bike(Vehicle):
    def __init__(self, max_speed, wheels, bike_type):
        super().__init__(max_speed, wheels)
        self.bike_type = bike_type


car = Car(200, 4, 'седан')
print("Максимальная скорость:", car.max_speed, "\nкол-во колес:", car.wheels, "\nкузов:", car.body)
bike = Bike(300, 2, 'мотокросс')
print("Максимальная скорость:", bike.max_speed,"\nкол-во колес:", bike.wheels, "\nтип:", bike.bike_type)
