from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for val in [r, g, b]:
            if isinstance(val, int) or 0 <= val <= 255:
                return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if isinstance(sides, tuple):
            for side in sides:
                side > 0
            return True

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        if self.sides_count == 12:
            return [self.__sides[0]]*self.sides_count
        else:
            return self.__sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius * 2)
        self.__radius = radius

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = 0

    def get_square(self):
        p = sum(self.get_sides()) / 2
        return (p * (p - self.get_sides()[0])) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides_length):
        super().__init__(color, *([sides_length] * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())