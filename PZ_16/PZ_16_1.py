"""Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
площади, длины окружности и диаметра."""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_square(self):
        print("Площадь круга:", 3.1428 * int(self.radius) * int(self.radius))

    def get_diameter(self):
        print("Диаметр круга:", self.radius * 2)

    def get_length(self):
        print("Длина круга:", 2 * 3.1428 * self.radius)


circle1 = Circle(5)

circle1.get_square(),
circle1.get_diameter()
circle1.get_length()
