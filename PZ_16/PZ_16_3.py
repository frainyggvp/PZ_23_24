import pickle


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_square(self):
        print("Площадь круга:", 3.1428 * int(self.radius) * int(self.radius))

    def get_diameter(self):
        print("Диаметр круга:", self.radius * 2)

    def get_length(self):
        print("Длина круга:", 2 * 3.1428 * self.radius)


def save_def(element, name):
    f = open(name, 'wb')
    pickle.dump(element, f)
    f.close()


def load_def(name):
    f = open(name, 'rb')
    element = pickle.load(f)
    print(element)


circle1 = Circle(5)
circle2 = Circle(2)
circle3 = Circle(10)

save_def(circle1, '1.bin')
load_def('1.bin')
save_def(circle2, '2.bin')
load_def('2.bin')
save_def(circle3, '3.bin')
load_def('3.bin')
