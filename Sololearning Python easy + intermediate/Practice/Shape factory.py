# Improving drawing application by adding and comparing two Shape objects.
# Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.
# The addition should return a new object with the sum of the widths and the heights of the operands, while the comparison should return the result of comparing the areas of the objects. 
class Shape:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height
    def __add__(self,other):
        return Shape(self.width + other.width, self.height +other.height)
    def __gt__(self,other):
        if self.width * self.height > other.width * other.height:
            return True
        else:
            return False

w1 = int(input("W1?"))
h1 = int(input("H1?"))
w2 = int(input("W2?"))
h2 = int(input("H2?"))

s1= Shape(w1, h1)
s2= Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1>s2)