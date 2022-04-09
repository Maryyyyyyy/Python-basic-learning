# **Python basic learning in sololearn**
- [**Python basic learning in sololearn**](#python-basic-learning-in-sololearn)
  - [1.  Sololearn intermediate - collection type](#1--sololearn-intermediate---collection-type)
    - [1.1 Python detect empty input (ticket)](#11-python-detect-empty-input-ticket)
    - [1.2 Tuple unpack (Square up)](#12-tuple-unpack-square-up)
    - [1.3 Tuples (contact search)](#13-tuples-contact-search)
    - [1.4 Job matching using set (You are qualified)](#14-job-matching-using-set-you-are-qualified)
    - [1.5 List comprehension (Ignore the vowels)](#15-list-comprehension-ignore-the-vowels)
    - [1.6 letter counter](#16-letter-counter)
  - [2. Sololearn intermediate - Functional programming](#2-sololearn-intermediate---functional-programming)
    - [2.1 Lambdas (How much?)](#21-lambdas-how-much)
    - [2.2 map and filter (get a raise/animal lifetime)](#22-map-and-filter-get-a-raiseanimal-lifetime)
    - [2.3 Generators (Generator)](#23-generators-generator)

## 1.  Sololearn intermediate - collection type 

### 1.1 Python detect empty input (ticket)
- notes in python for beginner
### 1.2 Tuple unpack (Square up)
- Only immutable (unchangable) objects can be used as keys to dictionaries 
- can use in or not in to determine whether a key is in a dictionary
- ` nums = {1: "a". 2: "b" }`  
1 is the key 
- get is the same as index, if key is not found, will return the second value in the racket. If the second argument is not specified, the value will be none 
- `pairs = {1: "apple", 2: "True"}` pairs.get(6,42) will return value 42
- Tuples are similar to list, immutable, created used parenthesis ("a", "b")
- We cannot reassign value in tuples 
### 1.3 Tuples (contact search)
- Tuples can be unpack by assigning each item in a collection to a variable 
- ` numbers = (1,2,3) a,b,c=numbers`  
reassign 1 to a, 2 to b and 3 to c
- a variable with * will take all the value that are left over
- ` numbers = (1,2,3, 4) a,b*,c=numbers` reassign 1 to a, 2,3 to b and 4 to c
### 1.4 Job matching using set (You are qualified)
- set is unordered, created by {}
- cannot be indexed
- can checked using in operator
- add(), remove()
- set can be combined using mathematical operation: union (|), intersection (&), difference (-), symmetric difference(^)
- intersection: items only in both 
- difference (-): items in first set but not second
- symmetric difference (^) : gets item in either set, not both
### 1.5 List comprehension (Ignore the vowels)
- list comprehension `[i*3 for i in range(5)]`
- if can be used in the list   
  ` [i**2 for i in range(10) if i**2 %2 ==0]`
### 1.6 letter counter 
- list: collection which is ordered and changable, allows duplicate members; 
- tuple: collection which is order and unchangable, allow duplicate members;
- set: collection which is unordered and unindexed, do not allow duplicate members;
- dictionary: collection which is ordered and changeable, no duplicate members. 

## 2. Sololearn intermediate - Functional programming

### 2.1 Lambdas (How much?)
- create the function on the fly using lambdas, it can pass a simple function as an argument to another function 
  ```
  def my_func (f,arg):
    return f(arg)
  my_func(lambda x: 2*x*x, 5)
  ```

### 2.2 map and filter (get a raise/animal lifetime)
- map takes a function and an iterable as arugments. It returns a new iterable with the function applied to each argument
  ```
  def add_five (x):
    return x+5
  nums = [11,22,33,44,55]
  result = list(map(add_five,nums))
  ```
- result will return [16,27,38,49,60]
- filter filters an iterable by leaving only the items that match a condition
  ```
  nums = [11,22,33,44,55]
  res= list(filter(lambda x: x%2 == 0, nums))
  print(res)
  ```
- res will return only [22,44]

### 2.3 Generators (Generator)
- Generator are created using functions and yield statement
- Generator is a type of iterables, like lists or tuples. Unlike lists, does not allow indexing with arbitary indices (mutable). Can be iterated through with for loops. 
  ```
  def countdown():
    i = 5
    while i >0:
      yield i
      i-=1 
  for i in countdown():
    print (i)
    ```
- It will print out 5 4 3 2 1, not in a list. 
- yield function will only print one item at a time. But the loop could be infinite. 

### 2.4 Decorator (Collecting reports)
- Decorators provide a way to modify function using other function 
- it can be written at the outside of a function 
- we can refer the written decorator as @decor in later lines 
  ```
  def decor(func):
    def wrap():
      print("============")
      func()
      print("============")
  return wrap()

  def print_text():
    print("Hello world")

  decorated = decor(print_text)
  decorated()
  ```
- @decor is the same as decor()

### 2.5 Recursion (Decimal to Binary)
- recursion is self-reference, functions calling themselves. 
- Example using factorial
  ```
  def factorial(x):
    if x ==1:
      return 1
    else:
      return x * factorial(x-1)
  ```
- Base case of recursive function is 1

 ### 2.6 *args and **kwargs (Making it work)
 - "* args" as function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function
   ```
    def function(named_arg, *args)
      print(named_arg)
      print(arg)
    function(1,2,3,4,5)
- It will return 
  ```
  1
  (2,3,4,5)
- It can be interpreted as 1 is stored as named_arg, the rest is stored together as tuples in args. 
- "** kwargs" allows you to handle named arguments that you have not defined in advance. 
- It returns a dictionary in which the keys are the argument names and the values are the argument values 
  ```
    def my_func(x, y=7, *args, **kwargs):
      print(kwargs)
      print(args)
    my_func(2,3,4,5,6, a=7, b=8)
  ```
- It will return 
  ```
  {"a":7, "b":8}
  (4,5,6)
  ```
- Kwargs recognize the a=7 and b=8 and convert them into dictionaries. Args recognize the unsure 4,5,6 and convert it into tuples
  