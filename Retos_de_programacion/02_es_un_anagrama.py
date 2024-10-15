'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
        -Comprobar que tengan el mismo numero de letras listo
        -Comprobar que tenga las mismas letras cantidad de letras iguales
        -Comprobar que tenga las misma cantidad de letras repetidas
        -Comprobar que esten en un orden diferente

 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    if palabra1 == palabra2:
        return False

    return sorted(palabra1) == sorted (palabra2)



print(anagrama("caas","casa"))

from collections import Counter

palabra1 = "casa"
palabra2 = "casa"
palabra1 = palabra1.lower()
palabra2 = palabra2.lower()
print(sorted(palabra1))

    #return sorted(palabra1) == sorted (palabra2)
