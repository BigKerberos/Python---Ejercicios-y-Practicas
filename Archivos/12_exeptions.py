### Exception Handling ###

number_one = 5
number_two = 1
number_two = "1"

# try except

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

# try except else finally

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: # Opcional
    #Se ejecuta si no se produce una excepción
    print("La ejecución continuá correctamente correctamente")
finally: # Opcional
    #Se ejecuta siempre
    print("La ejecución continuá")

# Excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido un ValueError")    
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError as error:
    print("Se ha producido el siguiente ValueError:")
    print(error)
#except TypeError as error:
except Exception as exeption:
    print("Se ha producido el siguiente TypeError:")
    print(exeption)



