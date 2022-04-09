# Given code defines a recursive function convert(), which convert its argument from decimal to binary
# fix the code by adding base case for the recursion and then take a number from user input and call the convert() function to output the result

def convert(num):
    if num == 1:
        return 1
    else: 
        return (num%2 + 10 * convert(num//2))

print(convert(int(input("What is sample input?"))))