### Dia 12 ###
from random import *

# Ejercicio 1 #

#1
def random_user_id():
    user = []
    for j in range(6):
        i = randint(1,3)
        if i == 1:
            value = randint(48,57)
        elif i == 2:
            value = randint(65,90)
        elif i == 3:
            value = randint(97,122)
        user.append(chr(value))
    user = "".join(user)
    return user

print(random_user_id())

                    
#2

def user_id_gen_by_user():
    user = []
    usuarios = []
    largo = input("Ingresa el numero de caracteres de la contraseña:")

    try:
        largo_int = int(largo)
    except:
        print("Error: El valor ingresado no es un número entero")

    numero_users = input("Ingresa el numero de usuarios que desea:")
    try:
        numero_users_int = int(numero_users)
    except:
        print("Error: El valor ingresado no es un número entero")

    for k in range(numero_users_int):
        for j in range(largo_int):
            i = randint(1,3)
            if i == 1:
                value = randint(48,57)
            elif i == 2:
                value = randint(65,90)
            elif i == 3:
                value = randint(97,122)
            user.append(chr(value))
        user_join = "".join(user)
        usuarios.append(user_join)
        user=[]
    
    return '\n'.join(usuarios)

print(user_id_gen_by_user())


def rgb_color_gen():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    return f'rgb({red},{green},{blue})'

print(rgb_color_gen())

# Ejercicio 2 #

#1
def list_of_hexa_colors():
    hexa = []
    for j in range(6):
        i = randint(1,2)
        if i == 1:
            value = randint(48,57)
        elif i == 2:
            value = randint(97,102)
        value = chr(value)
        hexa.append(value)
        value = 0
    hexa_join = "".join(hexa)
    return f"#{hexa_join}"

print(list_of_hexa_colors())

def list_of_rgb_colors():
    color = []
    for i in range(n):
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        rgb = f"rgb({red}, {green}, {blue})"
        color.append(rgb)
    return color

n=5
print(list_of_rgb_colors())

def generate_colors(tipo, cantidad):
    colors = []
    hexa = []
    if tipo == 'hexa' or tipo == 'Hexa':
        for k in range(cantidad):
            for j in range(6):
                i = randint(1,2)
                if i == 1:
                    value = randint(48,57)
                elif i == 2:
                    value = randint(97,102)
                value = chr(value)
                hexa.append(value)
                value = 0
            hexa_join = "".join(hexa)
            hexa_data = f"#{hexa_join}"
            colors.append(hexa_data)
            hexa.clear()
        return colors
        
    elif tipo == 'rgb' or tipo == 'RGB':    
        color = []
        for i in range(cantidad):
            red = randint(0,255)
            green = randint(0,255)
            blue = randint(0,255)
            rgb = f"rgb({red}, {green}, {blue})"
            colors.append(rgb)
        return colors
    
print(generate_colors('rgb', 1))

### Ejercicio 3 ###
def shuffle_list(list):
    shuffle(list)
    return list

comida = ['Huevo', 'Carne', 'Pescado', 'Frijoles']
print(shuffle_list(comida))

def random_number():
    number = []
    value = 0
    for j in range(7):
        value = randint(0,9)
        while str(value) in number:
            value = randint(0,9)
        number.append(str(value))
    number_join = "".join(number)
    return number_join

print(random_number())
