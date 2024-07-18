#pandas

import pandas as pd
f1=pd.read_csv("buzzers.csv")
print(f1)
###########################
#check for woring directiory
import os
with open("buzzers.csv") as raw_data:
    print(raw_data.read())
    
#reading csv data as lists
import csv 
with open("buzzers.csv") as raw_data:
    for line in csv.reader(raw_data):
        print(line)   
        
##################################
#reading csv data as a dictionaries
import csv
with open("buzzers.csv") as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
        
######################################
with open("buzzers.csv") as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights
#####################################
#pre requisite to decorrators
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)

#pre requisite to decorators
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)
################################
#passing function as argument to other function
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)

#############################################
#fuction returning other functions
def hello_function():
    def say_hi():
        return "hi"
    return say_hi
hello=hello_function()
hello()
#############################################
#program for cube
#need to use decorator
import time
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time of execution square is{total_time}")
    return result

################################

def cal_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time of execution square is{total_time}")
    return result
array=range(1,100000)
out_square=calc_square(array)
out_cube=cal_cube(array)

################################
#a python decorator is afunction  that takes in function
#and returns it by adding some funcctionality
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper 
decorate=uppercase_decorator(say_hi)
decorate()
##################################
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator 
def say_hi():
    return 'hello pratik'
say_hi()
####################################
#applying multiple decorators
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@split_string 
@uppercase_decorator 
def say_hi():
    return 'hi aniket'
say_hi()

####################################
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took{total_time}mil sec")
        return result
    return wrapper

@time_it 
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it 
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)
############################################

        