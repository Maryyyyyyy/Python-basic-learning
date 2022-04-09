# given string as input, output how many times each letter appears in the string.
# Data is stored in dictionary, with the letters as the keys, and the corresponding counts as the values 
#create program to take a string as input and output a dictionary which represent the letter count. 

string = raw_input("What is your input?")
letter = list(string)
count = []
for i in letter:
    count_number = letter.count(i)
    count.append(count_number)
count_dic = {}
for key in letter:
    for value in count:
        count_dic[key] = value
        count.remove(value)
        break
print(count_dic)
print(count)