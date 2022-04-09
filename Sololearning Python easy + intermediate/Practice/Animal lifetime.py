# take an input and anlysis how many animals are older than given number
# solution 1 using for in []
ages = [3,1,9,0.4,7,12,2,1.7, 5.7,42,6.7, 14.5, 21 ]
border = int(input("What is the age?"))
age = [x for x in ages if x > border]
print(len(age))
# solution 2 using filter function
ages = [3,1,9,0.4,7,12,2,1.7, 5.7,42,6.7, 14.5, 21 ]
border = int(input("What is the age?"))
animal_name = list(filter(lambda x: x > border, ages))
print(len(animal_name))
