# -*- coding: utf-8 -*-

Created on Tue Mar 19 08:25:25 2024

@author: rajwa
"""
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
sqr_list=list(filter(lambda x:(x*x),lst))
print(sqr_list)