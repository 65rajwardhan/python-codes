# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:25:25 2024

@author: rajwa
"""

a=5
b=3
print(a ** b)
'''assignment operator'''

x=0
x
x+=1
x

winner=None
print(winner is None) 

print(winner is not None)

winner=None
print('winner:',winner)
print('winner is None' ,winner is None)
print('winner is not None:',winner is None)
print(type(None))


num =int(input('Enter a number:'))
if num > 0:
 print (num)

#else in if statement
num =int(input('Enter another number:'))
if num < 0:
    print('its negative')
else:
    print('its not negative')


#the use of elif
savings=float(input("enter"))
if savings ==0:
    print("sorry no saving")
elif savings <500:
    print("well done")
elif savings <1000:
    print("thats tedy sum")
elif savings <10000:
    print("welcome sir")
else:
    print("thank you")
 
count=1
print("starting")
while count <=10:
    print(count)
    count+=1
    
#for loop
#loop over a set of values in a range
print("print values in range")
for i in range(2,10):
    print(i)
 
###########
print("only print code if iterations are correct")
num=int(input("enter the number"))
for i in range(0,16):
    if i==num:
        break
    print(i)
print("done")

#anonymous loop variables
for _ in range(0,10):
    print(".",end="aa")
    print()
    
for _ in range(0,10):
    print(".",end="aa")
 
 #for odd numbers
start, end=4,66  
#iterating each number in list
for num in range(start,end+1) :
    if num % 2!=0:
        print(num,end=" ")

#for even numbers
a=3
b=55
for num in range(a,b):
    if num%2==0:
        print(num,end=" ")
 
 #global varibles
x="awesome"
def my_function():
    print("python is "+x)
my_function()
    
#global and local variables
x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)
 
x=5
print(type(x))

#########
x=range(6)
print(type(x))

############
x={"name":"ram","age":21}
print(type(x))     

#assigning values
x=1
y=2,3
z=2+3j 
print(type(x))
print(type(y))
print(type(z))    
    
    #error 
str1="hello"
sre2=3
str3=str1+str2

#for multiple strings
x="this is python"
print(x)

#string slicing
x="this is python"
print(x[2:8])
#slicing from start
print(x[:10])
#slicing from end
print(x[7:])
#negative indexing
print(x[-10:-3])

#modifying string'
print(x.upper())
#x=x.upper()
print(x.lower())

#remove white space
x="  this is python"
print(x.strip())

#using replace
x="hello world"
print(x.replace("hello", "gello"))

#use of split
x="hello world"
print(x.split(" "))

x="hello world"
string1=x[::-2]
print(string1)

#searching string
x="this is python and it is very powerfull"
print(x.find("and"))

#string concatness
x="hell"
y="world"
print(x+y)

#to add white space
print(x+" "+y)

#string format
x=22

print(f"my name is antony and my age is{x}")

##############
quantity=3
item_no=4
price=77
print(f"i want {quantity} pieces of of item having no {item_no} its price is {price}")
#########
my_order="i want {} pieces and item no is {}and its price is{}"
print(my_order.format(quantity,item_no,price))

test="rule is \"raj\""
print(test)


#operation precedence
print(3*3+3/3-3)

"REMDAS"

#python list
lst=["cherry","apple","banana"]
print(lst)
#calling list items using index
print(lst[0])
print(lst[1])
#add item
lst.append("mango")
print(lst)
#clear list
lst.clear()
print(lst)
#copy list
lst=["cherry","apple","banana"]
lst2=lst.copy()
print(lst2)

#counts no of repeating items in list
lst=["cherry","cherry","banana"]
lst.count("cherry")

lst=[1,2,3]
lst2=[4,5,6]
lst.extend(lst2)
print(lst)

lst=["cherry","apple","banana"]
lst.insert(2,"mango")
print(lst)

lst=["cherry","apple","banana"]
lst.pop(2)
print(lst)

lst=["cherry","apple","banana"]
lst.remove("banana")
print(lst)

lst=["cherry","apple","banana"]
lst.reverse()
print(lst)


lst=["cherry","apple","banana"]
lst.sort()
print(lst)

#tuple
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])

x=["cherry","apple","banana"]
x[1]='kiwi'
#first convert into list
y=list(x)
y[1]='kiwi'
#convert list into tuple
x=tuple(y)
print(x)

x=("apple",2,"cherry")
print(x)

x=["cherry","apple","banana"]
print(x[1])

#to join two tuple
tup1=("a","b","c")
tup2=(1,2,3)
tup=tup1+tup2
print(tup)


#Dictionary
dict1={"brand":"maruti","model":"5645","year":2013}
print(dict1)

dict1={"brand":["maruti","mahindra","yamaha"],"Model":["a","b","c"],"Year":[2000,2001,2002]}
print(dict1)
print(len(dict1))
print(type(dict1))

dict1.get("model")
dict1.keys()

car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
x =car.keys()
print(x)
car["color"]="white"
print(car)
x=car.keys()
print(x)

#removing a dictionary element
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car.pop("model")
print(car)

#for accessing keys 

for x in car:
    print(car[x])
    
#for accessing keys and values

for key,value in car.items():
    print("%s == %s" % (key,value))

#copying dictionary
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }  
car2=car.copy()
print(car2)

#another way to copy
car3={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car4=dict(car3)
print(car4)

#nested dictionary the dict can comntain dictoneries

our_family={
    "child1":{"name":"ram","dob":"21-05-2003"},
    "child2":{"name":"akash","dob":"01:01:1001"}
    }
print(our_family)

#clear method to clear all elements 
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car.clear()
print(car)
#key method
x={'key','key2','key1'}
y=3
thisdict=dict.fromkeys(x,y)
print(thisdict)

#get values of dictionary
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car.get("model")
###########################
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car.items()

#display values of dictionary
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car.values()

#insert item to an dictionary
car={
     "brand":"Ford",
     "model":"mustang",
     "year":1969
     }
car.update({"color":"red"})
print(car)

#for loop

fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i=="banana"):
        break
    
fruits=["apple","banana","orange"]
for i in fruits:
    if(i=="banana"):
        break
    print(i)
    
#continue statement
fruits=["apple","banana","orange"]
for i in fruits:
    if i=="banana":
        continue
    print(i)

#####################
for x in range(2,6):
     print(x)      
#####################
for x in range(2,30,3):
     print(x)     
#############################     
#nested loop
a=["x","y","z"]
b=["d","e","f"]
for x in a:
        for y in b:
            print(x,y)
            
##########################
def my_function():
    print("hello")
my_function()

##########################

def my_function(name):
    print("hello " +name)
my_function("ram")

##########################

def my_function(name1,name2):
    print(name1+" pranit to "+name2)
my_function("hello", "world")

##########################
#arbitrary arguments

def my_function(*kids):
    print(kids[0]+" "+kids[2])
my_function("hell","to","go")

#########################
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='lala',mid='mohan',last='gogo')

############################
#calling function with default argument
#then it uses default values

def my_function(country="india"):
    print("i am from "+country)
    
my_function("norway")
my_function("brazil")
my_function()
my_function("russia")

###############################
#passing list as argument

fruits=["orange","apple","gauva"]
def my_function(fruits):
     for i in fruits:
         print(i)
my_function(fruits)

###############################

def my_function(x):
    return x*5
my_function(5)

#####################
#pass function
def my_function():
    pass

########################
#factorial of number
def factorial(x):
    if x==1:
        return 1 
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

#lambda function is a small anonymous function
#it can take any number of arguments
#but can have only one expression

def add(a):
    sum=a+10
    return sum
add(20)

add=lambda a:a+10
print(add(20))
####
add=lambda a,b:a+b
print(add(5,6))

#finding odd numbers from list
lst=[34,14,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2 !=0),lst))
print(odd_lst)

#finding even numbers from list
lst=[34,14,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

##taking square of numbers from list
lst=[44,2,4,7,8,77,8,9,43,5]
sqr_list=list(map(lambda x:(x**2),lst))
print(sqr_list)

#using if and elif
print("welcome to the roller coaster")
height=int(input("please enter your height in cm"))
if height>22:
    print("you are eligible")
    age=int(input("enter your age"))
    bill=0
    if age<20:
        print("your ticket prise is 100")
        bill=100
    elif age>20 and age<23:
        print("your tickit is 300")
        bill=300
    
    elif age>=23 and age<=33:
        print("your tickit is of 400")
        bill=400
    photo=(input("do u want photo y or n"))
    if photo=='y':
        bill+=3
        print(f"you need to pay {bill} in $")
    else:
        print("no")
    want_food=(input("you need food then say Y"))
    if want_food=='y':
        bill+=30
        print(f"your bill is{bill}")
    else:
        print("n")
else:
         print("you are not eligible")
        
##########################

height=float(input("enter your height in m :"))
weight=float(input("enter your weight in kg :"))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print(f"you are under weight and your BMI is{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"you are normal weight and your BMI is{BMI}")
elif BMI>25 and BMI<30:
    print(f"you are over weight and your BMI is{BMI}")
elif BMI>30 and BMI<35:
    print(f"you are obese and your BMI is{BMI}")
elif BMI>35:
    print(f"you are clinically obese and your BMI is{BMI}")
else:
    print("sorry")

##################################

lst1=[1,2,3,4,5] 
def is_duplicate(lat1):
      for i in range(len(lst1)-1):
          if(lst1[i]==lst1[i+1]):
              return True
      return False
print(is_duplicate(lst1))
       
#################################
def leap_year(year):
    if (year>0) and (year%100==0) or (year&400==0):
        return True
    return False
print(leap_year(2024))

##################################
#program to display mario pyramid

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
    
    for i in range(4):
        for j in range(4-i):
            print("#",end=" ")
        print()
        
        for i in range(4):
            for j in range(i+1):
                print("#",end=" ")
            print()
        
##################################
lst=[23,4,6,8,44,66,7,77]  
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("the minimum value is",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("the maximum  value is",max)
min_max(lst)

################################### 
#palindrome
def is_palindrome(input):
    if input=="":
        return "you entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
        return False
print(is_palindrome("onhjno"))

####################################

y=["boss","king","queen","worker"]
for x in y:
    if x=="boss":
        print("welcome boss")
    elif x=="king":
        print("jungle is yours")
    elif x=="queen":
        print("welcome")
    elif x=="worker":
        print("work fast")
else:
      print("go and sleep")
      
###############################
import string
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green','blue','purple','white','brave']
nouns=['apple','ball','pranit','panda']
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
number=random.randrange(0,100)
special_char=random.choice(string.punctuation)
password=adjectives+nouns+str(number)+special_char
print('your new password is:%s'% password)

#######################################
print('welome to password picker!')
while True:
     adjectives=random.choice(adjectives)
     nouns=random.choice(nouns)
     number=random.randrange(0,100)
     special_char=random.choice(string.punctuation)
     password=adjectives+nouns+str(number)+special_char
     print('your new password is:%s'% password)
     response=input('would you like to generate another password?type yes or no')
     if response=='n':
         break
  
#########################################
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#using list ccomprehension

lst=[num for num in range(0,20)]
print(lst)

####################################

names=['dada','mama','kaka']
lst=[i.capitalize() for i in names]
print(lst)

####################################
#list comprehension using if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

#########################################

lst=[f"{x}{y}"for x in range(3)for y in range(3)]
print(lst)

#########################################
#dictionary comprehension
dict={x:x*x for x in range(3)}
print(dict)

#################################
#generator
gen={x for x in range(10)}
print(gen)
for num in gen:
    print(num)

###############
gen=(x for x in range(3))
next(gen)
next(gen)

####################################
#function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
        print(num)
#############################
gen=range_even(8)
next(gen)
next(gen)

#############################
#changing generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
       
##############
#ele  appears to be a placeholders for an element
#fro an iterable the astrisk(*) is likely just 
#characters used to represent a placeholderor a wildcaed
#for instance you are not iterating over a list of elements:
#"ele*" can symboliz any element in the list 
#it is generic representation that corrospons to any specific syntax in python 
#or itertools

passwords=["aniket","akash","1234=4556"]
for password in hide(lengths(passwords)):
    print(password)   
    

##################################
#enumerates

lst=["milk","Egg","bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
    
#code using enumerates
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
#############################
#use of zip function
name=['dada','mama','kaka']
info=[9850,6032,9758]
for nm,inf in zip(name,info):
    print(nm,inf)

###########################
#use zip for mis match list
name=['dada','mama','kaka','baba']
info=[9850,6032,9758]
for nm,inf in zip(name,info):
    print(nm,inf)
##################

#zip longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9758]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
###############################
#use of fill value instead of none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9758]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
##3###################
#use of all()
lst=[2,0,5,-6,9]
if all(lst):
    print("all values are true")
else:
    print("there are zero values in list")
###############
lst=[2,3,0,6,9]
if all(lst):
    print("all values are true")
else:
    print("there are null values in list")
###############################
#use of any if any one non zero value
lst=[0,0,0,6,0]
if any(lst):
    print("it has some non zero values")
else:
    print("uselsee")
########################
lst=[0,0,0,0,0]
if any(lst):
    print("it has some values")
else:
    print("all values are null in list")
    
###############################
#use count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

###################################
#count start from one
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

##############################
#cycle()
import itertools
instructions=("eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
###############################
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=9):
    print(msg)
    
#######################
#combinations
from itertools import combinations
players=['john','jani','janardhan','ram','sham']
for i in combinations(players, 3):
    print(i)
    
################################
from itertools import permutations
players=['john','jani','janardhan','ram','sham']
for i in permutations(players, 3):
    print(i)
 
    
##################################
#product
from itertools import product
team_a=['rohit','virat','bumrah']
team_b=['sky','sachin','bhuvi']
for pair in product(team_a,team_b):
    print(pair)
    
################################
#shallow copy and deep copy
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0]=-10
print(list_a)
print(list_b)


import copy
li_a=[1,2,3,4,5]
li_b=copy.copy(li_a)

li_b[0]=-10
print(li_a)
print(li_b)

############################
#nested objects
import copy
li_a=[[1,2,3,4,5],[6,7,8,9,10]]
li_b=copy.copy(li_a)

li_a[0][0]=-10
print(li_a)
print(li_b)

###############################
#deep copy
li_a=[[1,2,3,4,5],[6,7,8,9,10]]
li_b=copy.deepcopy(li_a)
li_a[0][0]=-10
print(li_a)
print(li_b)
"""
##################################
