###Ejercicio 1###

#1
c1 = ()
print(type(c1))

#2
c2 = ("Carlos", "Steven","Leobardo")
c2_a= ("Bombon", "Burbuja", "Bellota")


#3
c3 = c2 + c2_a
print(c3)
c3_a = " ".join(c2+c2_a)
print(c3_a)

#4
c4 = len(c3)
print(c4)

#5
c5 = list(c3)
c5.append("Maria")
c5.append("Rafael")
c5 = tuple(c5)
print(c5)


### Ejercicio 2 ###

#1
c5 = list(c5)
parents = c5[-2:]
print(parents)

siblings = c5[0:-3]
print(siblings)

#2
fruits = ("Banana", "Apple", "Pineapple")
vegetables = ("Carot", "Pepper", "Pumpkin")
animal = ("Lion", "Rabbit", "Leopard","Kangaroo")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

#3
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

#4
e4_len = len(food_stuff_tp)
print(e4_len%2)
if e4_len%2 == 0:
    print("Es par")
    e4_int = int((len(food_stuff_tp))/2)
    e4_mit1 = food_stuff_tp[(e4_int-1):(e4_int+1)]
    print(e4_mit1)


else:
    print("Es impar")
    e4_int = int((len(food_stuff_tp))/2)
    e4_mit2 = food_stuff_tp[int((len(food_stuff_tp))/2)]
    print(e4_mit2)

#5

c5_1= food_stuff_tp[:3] 
c5_2 = food_stuff_tp[-3:] 
print(c5_1)
print(c5_2)

#6

del food_stuff_tp


#7
#print(food_stuff_tp)

#8
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)