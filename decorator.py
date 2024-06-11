# Passing function as an arguent to another function 
'''
def function1():
    print("Hello from function1 ")

def function2(func):
    print("Hello from function 2")
    func()

function2(function1)

# Returning function from another function 
def outer_func():
    print("Hello from outer function")
    def inner_func():
        print("Hello from inner function")
    
    return inner_func


func_var=outer_func()
func_var()


# Decorators in python 

import math
# This is our origginal function 

def square_root(num):
    sq_root = math.sqrt(num)
    return sq_root

def decorator_positive_number_only(ori_func):
    def wrapper (num):
        if num<0:
            print("Only positive numbers are allowed")
            raise ValueError
        else:
            sq_root = ori_func(num)
            return sq_root
    return wrapper

# Using a decorator 
new_decored_function= decorator_positive_number_only(square_root)
print(new_decored_function(9))
# print(new_decored_function(-9))

# Shorthand notation to use decorator 
@decorator_positive_number_only
def area_of_square_land(length):
    area= length**2
    return area

    
# new_area_decored_func= decorator_positive_number_only(area_of_square_land)
print("Area of lan with length 10 is:", area_of_square_land(10))
print("Area of lan with length -10 is:", area_of_square_land(-10))
'''

# WAP by using a custom defined timeit decorator to measure the execution time of any function
'''
HINT:
import time
current_time=time.time()
'''
import time

def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args, **kwargs)  #Calling the original function  

        stop =time.time()
        print(f"Execution time of function: {stop-start} seconds")
        
    return wrapper


@timeit
def number_generator(num):
    for i in range(num):
        print(i)
    
@timeit
def sum_of_list(input_list):
        sum=0
        for item in input_list:
             sum= sum+item 
        return sum 
        
        

number_generator(10)
input_list = [1,2,3,4,5]
sum_of_list(input_list)


    






















