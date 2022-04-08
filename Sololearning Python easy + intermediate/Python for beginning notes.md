# **Python for beginning notes** 
- [**Python for beginning notes**](#python-for-beginning-notes)
  - [1. Basic concept](#1-basic-concept)
  - [2. String](#2-string)
  - [3. Variables](#3-variables)
  - [4. Control flow](#4-control-flow)
  - [5. List](#5-list)
  - [6. Functions](#6-functions)
## 1. Basic concept
- print()
- multiplication is done by using *
- Division: /
- Integer: int()
- floats: float(), number with decimal
- strings: str(), are text enclosed in single or double quotes 
- **simple operation would return float value, // will return integer value without decimal**
- exponential: **  
- // floor division, reuturn integer
- % return the remainder of the division

## 2. String
- everything in quotes is a string, including numbers, **space in string is regarded as one element**
- escape character: \ 
- include a quote in a string, escape using \
` print('Brian\'s mother is great)` 
- create new line: \n
- create a tab: \t
- carriage return: \r 
- ''' automatically add newlines to string, quotes no need to be escaped as well 
- string can be concatenated by +  
` print("Spam" + "Egg")`   
output SpamEgg 
- Multiplying a string by an integer produces a repeated version of original string 

## 3. Variables 
- a = 2, 2 is assign to variables 
- a == 2, check if a is equal to 2 
- del: remove a variable, allow reassigned values to the variable 
- input(): usually processed as string, especially in python 3. python process input() as needed definition, use raw_input()
- x = x +3 is equal to x+ = 3. It is called in-place operators 
  
## 4. Control flow 
- Boolean value: True and false 
- Booleans are created when comparing values using ==, >, <, <=, >=.
- ! not equal to 
- String can be compare. A is smaller than b, as a is assigned to internal value 97, b as 98. 
- int(True) return to 1 and int(False) return to 0 
- if statement continue runs when the condition is true 
- else: run when if statement is false 
- Every if block can only have one else statement 
- elif chain together if and else 
- Boolean logic: and is true if both conditions evaluate to true
- Boolean logic: or is true if either of the condition is true and false if both are false 
- Boolean not: takes just one argument and invert it 
- order of operation: parentheses > exponentiation > multiplication/division > addition/substraction 
- while loop executed repeated while the condition is true (*iteration*)
- we can chain if inside while loop
- If the condition of while loop remain True, the loop will run indefinitely, causing infinite loop 
- break and continue can be used in while loop. The statement will return back to the while loop

## 5. List
- list is created by []
- can access certain item in list using index in square bracket
- list can make matrix  
  ` m = [[1,2,3],[4,5,6], [7,8,9]]`   
  m[1][2] return 3rd item of 2nd row
- list index start with 0 
- in can check if an item is in a particular list
- not x in list: can chekc if an item is not in a list
- for loop: iterate over a given sequence, such as lists or strings   
`for word in words: print word` 
- break and continue can be used in for loop as well 
- use for loop when the number of iteration is fixed; use while loop when the number of iteration isn't know and depends on some calculation and conditions 
- range(b): 0 to b-1, increment by 1 
- range(a,b): a to b-1, step can be used to control increment 
- use negative value in step to create list of decreasing numbers 
- list slice: get part of list using two colon-separated indices, without first number, we start with the beginning of the list. Without the second number, it is taken to the end 
- negative values can be used in list slicing. It counted from the end of the list 
- [::-1]: reverse a list 
- list operation  
`[1,2,3] + [4,5,6] = [1,2,3,4,5,6]
[1,2,3]*3 = [1,2,3,1,2,3,1,2,3]

## 6. Functions 
- len(): get the number of items in a list
- append(): add an item to the end of the list
- insert(): insert a new item at the given position in the list 
- index(): find the first occurrence of a list item and return its index
- max()/min()
- list.count(): return a count of how many times an item occurs in a list
- list.remove(): remove an item from a list
- list.reverse(): reverses items in a list
- clear(): remove all elements from the list
- copy(): return a copy of the list
- count(): return the number of elements with the specified value 
- extend(): add the elements of a list to the end the current list
- pop(): removes the element at the specified position 
- remove(): remove the first item with specified value
- sort(): sort the list
- join(): joins a list of string using specified seperator 
- split()
- replace(a,b ): replace one substring a in a string with another b 
- lower()/upper()
- 
- format() return 64-42-95  
`nums = "Numbers {2}-{0}-{1}". format(42,95,64)`
- def: make own function. Can define functions with more than one argument, separate them with commas 
- return statement 
- function can only return once, if need return multiple values, use a list
- comments are made by # 
- docstrings created by """ inside a function to explain the function