### Ejercicio 1 ###
'''
#1 
try: 
    age = int(input("Ingresa tu edad"))
except:
    print("No es un numero entero")

if age >= 18:
    print("Tienes edad para conducir")  
else:
    restante = 18 - age
    print(f"Necesitas {restante} años mas para conducir")


#2
my_age = int(input("Mi edad"))
your_age = int(input("Tu edad"))

if my_age > your_age and (my_age - your_age) != 1:
    diferencia = my_age - your_age
    print(f"Soy {diferencia} años mayor que tu")
elif my_age > your_age and (my_age - your_age) == 1:
    diferencia = my_age - your_age
    print(f"Soy {diferencia} año mayor que tu")
elif my_age == your_age:
    print("Tenemos la misma edad")
elif my_age < your_age and (your_age - my_age) == 1:
    diferencia = your_age - my_age
    print(f"Eres {diferencia} año mayor que yo")
else:
    diferencia = your_age - my_age
    print(f"Eres {diferencia} años mayor que yo")


#3
try: 
    a = float(input("Ingresa a"))
    b = float(input("Ingresa b"))
except:
    print("No ingresaste un numero")

if a > b:
    print(f"{a} es mayor que {b}")
elif a == b:
    print(f"{a} es igual que {b}")    
else:
    print(f"{a} es menor que {b}")   


### Ejercicio 2 ###

#1
try: 
    score = int(input("Ingresa la calificacion del estudiante"))

except:
    print("No ingresaste un numero")

if score >= 90:
    print("Tu calificacion es A")
elif score >=70:
    print("Tu calificacion es B")
elif score >=60:
    print("Tu calificacion es C")
elif score >=50:
    print("Tu calificacion es D")
else:
    print("Tu calificacion es F")

#2
mes = input("Ingresa el mes actual")
otoño = ["Septiembre", "Octubre", "Noviembre"]
invierno = ["Diciembre", "Enero", "Febrero"]
primavera = ["Marzo", "Abril", "Mayo"]
verano = ["Junio", "Julio", "Agosto"]

if mes in otoño:
    print("Es otoño")
elif mes in invierno:
    print("Es invierno")   
elif mes in primavera:
    print("Es primavera")
elif mes in verano:
    print("Es verano")
else:
    print("No ingresaste un mes")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input("Ingresa una fruta")

if fruta in fruits:
    print("Esa fruta ya esta en la lista")
else:
    fruits.append(fruta)
    join_list = ", ".join(fruits)
    print(f"Esta es la nueva lista de frutas: {join_list}")
'''
 ### Ejercicio 3 ###
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


if "skills" in person:
    e1_len = len(person["skills"])
    if e1_len % 2 == 0:
        #print("Es par")
        e1_int = int((len(person["skills"]))/2)
        e1_mit1 = person["skills"][(e1_int-1):(e1_int+1)]
        print(f"Las habilidades que se encuentran a la mitad son: {e1_mit1}")


    else:
        #print("Es impar")
        e1_int = int((len(person["skills"]))/2)
        e1_mit2 = person["skills"][int(e1_len/2)]
        print(f"La habilidad que se encuentra a la mitad es: {e1_mit2}")
else:   
    print("No hay una llave llamada skills")

if "skills" in person:
    print("Python se encuentra entre las habilidades") if "Python" in person["skills"] else print("Python no se encuentra entre las habilidades")
else:
    print("No hay una llave llamada skills")

'''
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
'''

if sorted(person["skills"]) == sorted(['Python', 'React']):
    print("El es un frontend developer")
elif sorted(person["skills"]) == sorted(['Node', 'Python', 'MongoDB']):
    print("El es un backend developer")  
elif sorted(person["skills"]) == sorted(['JavaScript', 'React', 'Node', 'MongoDB', 'Python']):
    print("El es un fullstack developer")  
else:
    print("No funciono... o si")

'''
 * If the person is married and if he lives in Finland, print the information in the following format:    
Asabeneh Yetayeh lives in Finland. He is married.
'''
if person["is_married"] and 'Finland' in person["country"]:
    print(f"{person['first_name']} {person['last_name']} vive en {person['country']}. Y el es casado")
elif person["is_married"]:
    a = person["country"]
    print(f"{person['first_name']} {person['last_name']} esta casado pero vive en {person['country']}")
elif 'Finland' in person["country"]:
    print(f"{person['first_name']} {person['last_name']} vive en Finland pero no esta casado")
else:
    print(f"{person['first_name']} {person['last_name']} no vive en Finland y no esta casado")
