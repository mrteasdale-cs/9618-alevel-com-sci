class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def describe(self):
        return f"This is a circle with radius {self.radius}."

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"This is a rectangle with width {self.width} and height {self.height}."

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())
print(circle.describe())
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print(rectangle.describe())
