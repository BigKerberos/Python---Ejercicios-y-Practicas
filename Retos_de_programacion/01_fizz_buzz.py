### 1. El famoso "FIZZ BUZZ" ###

'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for index in range(1,101):
    fizz = index % 3
    buzz = index % 5

    if fizz == 0 and buzz == 0:
        print("fizzbuzz")
    elif fizz == 0:
        print("fizz")
    elif buzz == 0:
        print("buzz")
    else:
        print(index)
    print("")

    
