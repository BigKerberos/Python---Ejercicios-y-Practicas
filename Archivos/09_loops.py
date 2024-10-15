### Loops ###

# While

my_condition = 0

while my_condition < 10 :
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual a 10")
print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break 

    print(my_condition)

print("La ejecución continua")

# FOR

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else: 
    print("El bucle for para mi diccionario ha finalizado")

print("La ejecución continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else: 
    print("El bucle for para mi diccionario ha finalizado")

