#Given code defines a function isPrime(x) which return true if x is Prime
#Create a generator function primeGenerator(), that will take two numbers as arguments and use the isPrime() function to output the prime numbers in given range 
#Output as list
# Solution 1 using list.append()
def isPrime(x):
    """prime number is the number that can only be divided by 1 and itself """
    if x<2:
        return False
    elif x ==2:
        return True
    for n in range (2,x):
        if x%n ==0:
            """if any remainder is 0, it means it can be completely divided, not prime"""
            return False
    return True 

def primeGenerator(a,b): 
    prime_list= []
    for i in range(a,b):
        if isPrime(i) is True:
            prime_list.append(i)
    return prime_list

f= int(input("what is the first number?"))
t= int(input("what is the second number?"))

print(primeGenerator(f,t))

# Solution 2 using yield function 
def isPrime(x):
    """prime number is the number that can only be divided by 1 and itself """
    if x<2:
        return False
    elif x ==2:
        return True
    for n in range (2,x):
        if x%n ==0:
            """if any remainder is 0, it means it can be completely divided, not prime"""
            return False
    return True 

def primeGenerator(a,b): 
    for i in range(a,b):
        if isPrime(i) is True:
            yield i 

f= int(input("what is the first number?"))
t= int(input("what is the second number?"))

print(list(primeGenerator(f,t)))