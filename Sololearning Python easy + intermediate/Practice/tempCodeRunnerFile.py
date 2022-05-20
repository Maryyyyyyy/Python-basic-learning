ages = [3,1,9,0.4,7,12,2,1.7, 5.7,42,6.7, 14.5, 21 ]
border = int(input("What is the age?"))
age = [x for x in ages if x > border]
print(len(age))