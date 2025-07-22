# ---------- Name of Variable ----------
# abc

lower_underscore = '' 
# All varible, function, module, method, commonly want modify

UPPER_UNDERSCORE = '' 
# Constant value, this value no need to modify

CamelCase = '' 
# Name for class

_ = '' 
# None

_private = '' 
# Private, Not import of import *

__private = '' 
# This variable just use in class, can't use in outside the class. 
# It will change name to '_ClassName__private', if use this name you also can use in outside class.

__dunderscore__ = '' 
# Magic methon, never use this name for your program


# ---------- Type of Data ----------


int() # x = 20 
# integer

float() # x = 20.5 
# float number

str() # x = "Hello World" 
# just text

complex() # x = 1j 
# have text and number

list() # x = ["apple", "banana", "cherry"] 
# list

tuple() # x = ("apple", "banana", "cherry") 
# tuple

range() # x = range(a,b,c) 
# is a number of a range.
# If just a, a is start form 0 until a-1.
# If have a and b, a is start number, b is amount of count. 
# Else, a is start number, b is amount of count, c is interval of number list.

dict() # x = {"name" : "John", "age" : 36}

set() # x = {"apple", "banana", "cherry"}

frozenset() # x = frozenset({"apple", "banana", "cherry"})

bool() # x = True/False
# True or False

bytes() # x = b"Hello"

bytearray() # x = bytearray(5)

memoryview() # x = memoryview(bytes(5))

None() # x = None
#Nothing


# ---------- Calculation ----------


a = 1 + 1 
# Addition

b = 1 - 1 
# Minus

c = 1 * 1 
# Multiple

d = 1 / 1 
# Divide

a += 1 
# Addition yourself

b -= 1 
# Minus yourself

c *= 1 
# Multiple yourself

d /= 1 
# Divide yourself

e = 1 ** 1 
# Power for

f = 1 // 1 
# Divisible, without number of behind dot

g = 1 % 1 
# Remainder, Remainder is the integer "left over" after dividing one integer by another to produce an integer


# ---------- Condition ----------


a == b 
# Two variable are same will True

a != b 
# Two variable are not same will True

a < b 
# a is small than b will True

a <= b 
# a is small or equal than b will True

a > b 
# a is greater than b will True

a >= b 
# a is greater or equal than b will True

a in ['a','b','c']
# a is in the list will True

while True:

    a = input('Enter: ')
    try:
        a = float(a)
    except ValueError:
        print('error')
        continue
    break


# ---------- List ----------


xyz = [] 
# Normal list, never name your list be 'list', probaly make some bug

xyz[0]
# the first value for the list

xyz[-1]
# the last value for the list

len(xyz)
# amount of value in the list

sum(xyz)
# sum of value in the list

xyz.append(a)
# put value of 'a' at the last

xyz.clear()
# clear all value in this list

xyz.insert(a,b)
# insert value of 'b' at position 'a'

xyz.remove(a)
# remove value of 'a' in the list

del xyz[0]
# delete first value in the list

abc = {} 
# dictionary, never name your dictionary be 'dict', probaly make some bug


# ---------- If ----------


if a == b: # Condition_1
    print()  # Must have Tab front your command
elif a < b: # Condition_2 when Condition_1 is False
    print()
else: # When all condition are False
    print()


# ---------- Base command ----------


print( a ) 
# print value of variable a

print( a + b ) 
# if a and b are number, then print value within calculation, else print a and b with string

print( 'abc' )
# print abc with string

print( f'abc {a}' , end = '\n')
# F-string, in {} be normal variable another will be string

print( end = '\n' )
# 'end' is a parameter for print, '\n' is a normal 'end'

print( end = '' ) 
# text in '' will put after the output, if with empty, will didn't change row

print( end = '\r' )
# '\r' is all output will in one row until you change 'end',
# if have new print that will replace of that

print( sep = '' )
# text in '' will put before the output

input()
# can use for let user input text or number
# in () can put text, output that before user input
# this command commonly use for value of variable


# ---------- Loop ----------


while a < 1:
    print()
# while loop when condition is True, if False will end the loop

while True: # also can straightly put True in condition, but it will never stop until 'break'
    print()

    if a == 1:
        break # end the loop
    elif a < 1:
        continue # enter next loop

    print()

for i in range(a,b,c): 
# i is counter of loop
    print()

    if i == 1:
        break # end the loop
    else:
        continue # enter next loop


# ---------- Function ----------


def Test_Function(d=1,e=2): # can put the default value for parameter
# define a lot of command to a function
# () is parameter for function
# variable in () just affect it's function
    print(d,e) # a lot of command

Test_Function(2,3)
# normally put value of parameter

Test_Function(1)
# put one value for parameter, if parameter have default value, will replace first parameter
# else will error

Test_Function(d=4,e=5)
# also can put value to each variable

Test_Function(e=6,d=7)
# no need to follow queue

