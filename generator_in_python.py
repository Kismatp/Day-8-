'''

# Definition of geneator in python 
def my_generator(num1):
    for i in range(num1):
        yield i

# CAlling generator function 
my_iterator= my_generator(5)
print(my_iterator)

# Accesing generator elements using next() method  

print(next(my_iterator))
print(next(my_iterator))


# Accesing generator elements using for loop 
for num in my_iterator:
    print(f"Using for loop: {num}")

'''

# creating generator using generator expression
my_generator_from_gen_expr = (i for i in range(5))
for val in my_generator_from_gen_expr:
    print(f"Using generator expression: {val}")





