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
    return element


circle1 = Circle(5)
circle2 = Circle(2)
circle3 = Circle(10)

save_def(circle1, '1.bin')
el1 = load_def('1.bin')
save_def(circle2, '2.bin')
el2 = load_def('2.bin')
save_def(circle3, '3.bin')
el3 = load_def('3.bin')

el1.get_square()
el1.get_diameter()
el1.get_length()
print('\n')
el2.get_square()
el2.get_diameter()
el2.get_length()
print('\n')
el3.get_square()
el3.get_diameter()
el3.get_length()
