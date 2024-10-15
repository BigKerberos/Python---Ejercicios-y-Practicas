# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 358
print(my_int_variable)

my_str_to_int_variable = str(my_int_variable)
print(my_str_to_int_variable)
print(type(my_str_to_int_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print
print(type(print(my_string_variable, my_str_to_int_variable, my_bool_variable)))
print("Este es el valor de:", my_bool_variable)
# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. ¡No uses mucho esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo", name,surname,"mi edad es", age, "y mi alias es:", alias)
print(type(age))

#Sistema sencillo de input

'''
name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
'''

#Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

#¿Forzamos el tipo? No...
address: str = "Mi direccion"
address = True
address = 1
address = 1.5
print(type(address))
