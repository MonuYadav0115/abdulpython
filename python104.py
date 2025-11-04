class Rectangle():
    def __init__(self):
        self.length = 10
        self.breadth = 5

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length +self.breadth)

r = Rectangle()
print("length",r.length)
print("Breadth",r.breadth)
print("area",r.area())
print("perimeter",r.perimeter())