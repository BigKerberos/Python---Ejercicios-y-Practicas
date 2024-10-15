
### Funciones de orden superior ###
'''  
## Función como parámetro
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

## Closure python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

## Python Decorators

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

print('')
## Let us implement the example above with a decorator
'''
#This decorator function is a higher order function
#that takes a function as a parameter

'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

def print_decorator(function):
    def wrapper():
        print("Executing the function...")
        return function()
    return wrapper


@uppercase_decorator
@print_decorator
def farewell():
    return 'Goodbye, see you soon!'

print(farewell())  # Executing the function... \n GOODBYE, SEE YOU SOON

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
'''
# Decorador que agrega un signo de exclamación al resultado
def add_exclamation_decorator(function):
    def wrapper():
        result = function()
        return result + "!"
    return wrapper

# Decorador que convierte el resultado en mayúsculas
def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

# Decorador que imprime mensajes antes y después de ejecutar la función
def print_decorator(function):
    def wrapper():
        print("Ejecutando la función...")
        result = function()
        print("La función ha sido ejecutada.")
        return result
    return wrapper

# Encadenamos los decoradores
@print_decorator
@add_exclamation_decorator
@uppercase_decorator
def greet():
    return "hello world"


print(greet())

### Built-in Higher Order Functions

## Python - Map Function

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

## Python - Filter Function

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

## Python - Reduce Function

from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

def multiplicar(a, b):
    return a * b

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usar reduce para multiplicar todos los números
resultado = reduce(multiplicar, numeros)

print(resultado)  # Salida: 120


#### Exercises: Day 14 ####

### Exercises: Level 1

#1


#2


#3


#4


#5


#6


### Exercises: Level 2

#1


#2


#3


#4


#5


#6


#7


#8


#9


#10


#11


#12


#13


#14


#15


### Exercises: Level 3

#1
