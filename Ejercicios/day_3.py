### Day 3 ###

import math

#4
age = 25
height = 1.70
num_complex = 4j

triangle_base = float(input ("Ingresa la base del triangulo"))
triangle_height = float(input ("Ingresa la altura del triangulo"))
triangle_area = (triangle_base * triangle_height) / 2
print(f"El area del triangulo es {triangle_area}")

#5
side_a = float(input ("Ingresa el primer lado"))
side_b = float(input ("Ingresa el segundo lado"))
side_c = float(input ("Ingresa el tercer lado"))
perimeter_triangle = side_a + side_b + side_c
print(f"El perimetro del triangulo es {perimeter_triangle}")

#6
rectangle_lenght = float(input ("Ingresa el largo del rectangulo"))
rectangle_width = float(input ("Ingresa la anchura del rectangulo"))
rectangle_area = rectangle_width * rectangle_lenght
rectangle_perimeter = 2*(rectangle_width + rectangle_lenght)
print(f"El area del rectangulo es {rectangle_area}")
print(f"El perimetro del rectangulo es {rectangle_perimeter}")

#7
import math

pi = math.pi
circle_radius = float(input("Ingresa el radio del circulo"))
circle_area = (pi * circle_radius) ** 2
circle_perimeter = 2 * pi * circle_radius
print(f"El area del circulo es {circle_area}")
print(f"El perimetro del circulo es {circle_perimeter}")

#8
'y= 2x-2'

m_8 = 2
intercept_x = 1
intercept_y = -2

#9
'(2,2) (6,10)'

x1=2
y1=2
x2=6
y2=10

m_9=(y2-y1)/(x2-x1)

euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(f"La pendiente es de {m_9}")
print(f"La distancia euclidiana es de {euclidean_distance}")

#10
comparative = m_8 > m_9
print(comparative)


#11
'y = x^2 + 6x + 9'

def x_igual (a, b, tolerancia=1e-9):
    return abs(a - b) < tolerancia

x1 = float(input("Ingresa el valor de x"))
y1= x1** 2 + 6 *x1 + 9
x0 = 0.0
y0 = x0** 2 + 6*x0 + 9

while not x_igual(y0, 0.0) and x0 < 5.0 :
    x0 = x0 + 0.1
    y0 = x0** 2 + 6*x0 + 9
    
x0 = 0.0
y0 = x0** 2 + 6*x0 + 9

while not x_igual(y0, 0.0) and x0 > -5.0 :
    x0 = x0 - 0.1
    y0 = x0** 2 + 6*x0 + 9
    


print(f"El valor de x para que y sea cero es: {x0}")
print(f"El valor de y es: {y1}")


#12
print(len("Python")==len("Dragon"))

#13
print("on" in ("Python" and "Dragon"))

#14
print("jargon" in "I hope this course is not full of jargon")

#15
if "on" in ("Python" and "Dragon"):
    print(False)

#17
try:
    number_even = input("Ingresa un numero")
    number_even = float(number_even)
    if (number_even % 2) != 0:
        print("Es un numero impar o un numero con decimales")
    elif (number_even % 2) == 0:
        print("Es un numero par")
except ValueError:
    print("No es un numero")
except TypeError:
   print("No es un numero")


#18

x1, x2 = 7.0, 3.0

result = x1 // x2

print(int(result))

#19

print(type(10)==type("10"))

#20
print(int(9.8))
print(int(9.8)==10)

#21

hours = float(input("Ingresa las horas trabajadas"))
rate_per_hour = float(input("Ingresa la paga por hora"))

result = hours * rate_per_hour

print(f"Tu paga es de ${int(result)} pesotes")

#22

years = float(input("Ingresa el numero de años"))

seconds = years * 365* 24 * 60 *60

print(f"Viviras por {int(seconds)} segundos.")

#23
for i in range(1,6):
    print(f"{i} {1} {i} {i**2} {i**3}")

