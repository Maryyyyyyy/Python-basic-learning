# Make a function cal(), that will take the side length of a square as its argument and return the perimeter and area using tuple. 
sample = int(input("What is the length of square?"))
def cal(a):
    perimeter = 4 * a 
    area = a**2
    output = list[("Perimeter:", perimeter), ("Area:", area)]
    return output

print(cal(sample))