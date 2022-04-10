# Making a drawing application which has a shape base class
# Inherit the rectangle class from Shape. And then define the perimeter method in the Rectangle class, printing the perimeter of the rectangle

class Shape:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def area(self):
        print(self.width * self.height)

class Rectangle(Shape):
    def perimeter(self):
        self.perimeter = 2* (self.width+self.height)
        print(self.perimeter)
    
w = int(input("What is the width?"))
h = int(input("What is the height?"))

r = Rectangle(w,h)
r.area()
r.perimeter()