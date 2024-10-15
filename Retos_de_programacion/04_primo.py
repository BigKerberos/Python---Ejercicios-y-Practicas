### ¿ES UN NUMERO PRIMO? ###
'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 PRIMO: Número entero, por convención mayor que uno, que solo es divisible por sí mismo y por la unidad; por ejemplo, 5, 7, etcétera.
 '''

def es_primo(numero):
    divisores = []

    if numero < 2:
        return False,divisores

    for i in range(2,int(numero/2)+1):
        if numero % i == 0:
            divisores.append(i)

    if len(divisores)>0:
        return False,divisores    
    
    return True, divisores
            

numero= 4

es_primo_flag, divisores = es_primo(numero)

if es_primo_flag:
    print(f"{numero} es un numero primo")
    
else:
    print(f"{numero} no es un numero primo. Divisores: {divisores}")

n=1
list_primos = []
for index in range(0,100):
    check, divisores = es_primo(index)
    if check:
        list_primos.append(index)

str_primos = "  ".join(map(str, list_primos))
print(f"Estos son los numero primos de 1 al 100: {str_primos}")








