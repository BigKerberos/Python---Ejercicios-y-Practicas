### Día 13 - Comprensión de listas ###

### Ejemplos ###
'''
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22


def power(x):
    return lambda n : x ** n

cube = power(3)(2)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32


### Ejercicios ###

#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_cero_list = [number for number in numbers if number <=0]
print(negative_and_cero_list)

#2

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [number for biglist in list_of_lists for sublist in biglist for number in sublist]
print(flatten_list)


#3

list_of_tuples = [(i , i** 0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatt_list = [[grandes.upper(),(grandes.upper()[0:3]),segundos.upper()] for biglist in countries for sub_list in biglist  for grandes in sub_list[:1] for segundos in sub_list[1:2]]
print(flatt_list)
#output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_countries = [{'country':primario.upper(),'city':secundario.upper()} for biglist in countries for subtupla in biglist for primario in list(subtupla)[:1] for secundario in list(subtupla)[1:2]]
print(dict_countries)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated = [f'{primario} {secundario}' for biglist in names for sublist in biglist for primario in list(sublist)[:1] for secundario in list(sublist)[1:2]]
print(concatenated)
'''
#7
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(1,2,3,4))
