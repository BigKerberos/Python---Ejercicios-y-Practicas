### LA SUCESION DE FIBONACCI ###
'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''

n0 = 0
n1 = 0
n2 = 1

for index in range(0,50):
    print(n0)
    n0= n1 + n2 
    n2 = n1
    n1 = n0
    