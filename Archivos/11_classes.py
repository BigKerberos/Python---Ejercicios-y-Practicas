### Classes ###
'''
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name = "N/A", surname = "N/A"):
        self.name = name
        self.surname = surname

my_person = Person("Brias", "Moure")
print(f"{my_person.name} {my_person.surname}")
print(my_person.name)

class Person:
    def __init__(self,):
        self.name = "Brais"
        self.surname = "Moure"

my_person = Person()
print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self,name, surname):
        self.full_name = f"{name} {surname}"

my_person = Person("Brias", "Moure")
print(my_person.full_name)



class Person:
    def __init__(self,name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Brias", "Moure")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Brias", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 777
print(my_other_person.full_name)


class Person:
    def __init__(self,name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"# Propiedad publica
        self._name = name # Propiedad privada
        self._surname = surname

        def get_name (self):
            return self._name

    def walk (self):
        print(f"{self._name} esta caminando")

my_person = Person("Brias", "Moure")
print(my_person._name)
my_person._name = "Steve"
print(my_person._name)
my_person.walk()
'''

class Persona:
    # Constructor, se llama cuando se crea una instancia de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
    
    # Método que define un comportamiento
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear una instancia (objeto) de la clase Persona
persona1 = Persona("Carlos", 30)

# Acceder a los atributos
print(persona1.nombre)  # Carlos
print(persona1.edad)    # 30

# Llamar a un método
persona1.saludar()  # Hola, me llamo Carlos y tengo 30 años.
persona2 = Persona("Ana", 25)  # Crea otro objeto
persona2.saludar() 

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llama al constructor de la clase padre
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando para el grado {self.grado}.")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Laura", 20, "Matemáticas")
estudiante1.saludar()  # Heredado de Persona
estudiante1.estudiar()  # Método específico de Estudiante
import math as m

class circulo:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return m.pi * self.radius ** 2

circulo1 = circulo(35)

print(circulo1.area())

class rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def area(self):
        return self.longitud * self.ancho
    
    def perimetro(self):
        return self.longitud * 2 + self.ancho * 2
    
    def es_cuadrado(self):
        return self.longitud == self.ancho

rectangulo1 = rectangulo(13,15)

print(rectangulo1.area())
print(rectangulo1.perimetro())
print(rectangulo1.es_cuadrado())


#E3
class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo+= cantidad
        return f"Su saldo actual es de: {self.saldo} pesos"

    def retirar(self, cantidad):
        if (self.saldo-cantidad) < 0:
            return "No hay saldo suficiente"
        else:
            self.saldo -= cantidad
            return f"Tu saldo actual es de {self.saldo} pesos"
    
    def mostrar_saldo(self):
        return f"Tu saldo actual es de: {self.saldo} pesos"

cuenta_juan = CuentaBancaria("Juan")

# Depositar 1000
print(cuenta_juan.depositar(1000))

# Mostrar saldo
print(cuenta_juan.mostrar_saldo())  # Saldo actual: 1000

# Retirar 500
print(cuenta_juan.retirar(500))

# Mostrar saldo
print(cuenta_juan.mostrar_saldo()) # Saldo actual: 500

# Intentar retirar una cantidad mayor al saldo disponible
print(cuenta_juan.retirar(600))  # Fondos insuficientes

# Mostrar saldo nuevamente
print(cuenta_juan.mostrar_saldo())