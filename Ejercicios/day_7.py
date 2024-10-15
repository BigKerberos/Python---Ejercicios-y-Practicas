### Ejercicio 1 ###

#1
'''
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(A)
print(B)
c1 = len(it_companies)
print(c1)

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update(["BMW","Lenovo","Sony"])
print(it_companies)

#4
print(len(it_companies))
it_companies.pop()
print(len(it_companies))

#5
it_companies.remove("Apple")
print(it_companies)
'it_companies.remove("Apple")' # Error
it_companies.discard("Apple") #No Error

### Ejercicio 2 ###

#1
c1 = A.union(B)
print(c1)

#2
c2 = A.intersection(B)
print(c2)

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
c5_1 = A.union(B)
c5_2 = B.union(A)
print(c5_1)
print(c5_2)

#6
print(A.symmetric_difference(B))

#7
del A, B, it_companies
#print(A, B, it_companies)
'''
### Ejercicio 3 ###

#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
set_age = set(age)
print(len(age))
print(len(set_age))
print(len(age)>len(set_age))

#2
    #String: Tipo de variable, no es un conjunto
    #List: Conjunto de variables ordenados, se puede añadir y borrar datos
    #Tuple: Conjunto de datos ordenados, no se puede añadir y borrar nuevos datos
    #Set: Conjunto de datos no ordenados, se puede añadir y borrar datos, no se pueden duplicar datos

#3
sentence = "I am a teacher and I love to inspire and teach people"
sentence = set(sentence.split())
print(len(sentence))

