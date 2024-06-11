# Reduce function 
# we have add all the elements of a list 
list1= [ 1,2,3,4,5]

from functools import reduce #---> Must be always in the top of a program 
def add_two_num(num1,num2):
    return num1+num2
sum=0

cumulative_sum= reduce(add_two_num,list1)

print(f"The cumulative sum is: {cumulative_sum}")



