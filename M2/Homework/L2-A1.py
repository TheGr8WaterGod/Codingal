
class Polygon:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        formula = "side × side"
        value = self.side * self.side
        print(f"{self.name} area formula: {formula}")
        print(f"Area = {value} sq. units")
        return value


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        formula = "length × width"
        value = self.length * self.width
        print(f"{self.name} area formula: {formula}")
        print(f"Area = {value} sq. units")
        return value


class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        formula = "½ × base × height"
        value = 0.5 * self.base * self.height
        print(f"{self.name} area formula: {formula}")
        print(f"Area = {value} sq. units")
        return value


# Example usage
s = Square(5)
s.area()

r = Rectangle(10, 4)
r.area()

t = Triangle(6, 3)
t.area()
