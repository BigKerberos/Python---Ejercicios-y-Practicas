### Day 2: 30 Days of python programming ###


'E1'
first_name = "Brandon"
last_name = "Lagunas"
full_name = "Brandon Lagunas"
country = "Mexico"
city = "Zapopan"
age = 25
year = 1998
is_married = "no"
is_true = True
is_light_on = False 
height, weight, eye_color = 1.70, 70, "Brown"

'E2'
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(height))
print(type(weight))
print(type(eye_color))

print(len(first_name))
print(len(last_name))
comparative_fn_ln = len(first_name) >= len(last_name)
print(comparative_fn_ln)

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

import math

pi = math.pi

radius = 30
area_of_circle = (pi*radius)**2
circum_of_circle = 2*pi*radius

print(area_of_circle)
print(circum_of_circle)
'''
first_name = input("Primer nombre")
last_name = input("Apellido")
country = input("Pais")
age = input("Edad")

print(first_name)
print(last_name)
print(country)
print(age)
'''
help('keywords')
help('try')