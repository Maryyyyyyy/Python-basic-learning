# **Python basic learning in sololearn**
- [**Python basic learning in sololearn**](#python-basic-learning-in-sololearn)
  - [1.  Sololearn intermediate - collection type](#1--sololearn-intermediate---collection-type)
    - [1.1 Python detect empty input (ticket)](#11-python-detect-empty-input-ticket)
    - [1.2 Tuple unpack (Square up)](#12-tuple-unpack-square-up)
    - [1.3 Tuples (contact search)](#13-tuples-contact-search)
    - [1.4 Job matching using set (You are qualified)](#14-job-matching-using-set-you-are-qualified)
    - [1.5 List comprehension (Ignore the vowels)](#15-list-comprehension-ignore-the-vowels)
    - [1.6 letter counter](#16-letter-counter)

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