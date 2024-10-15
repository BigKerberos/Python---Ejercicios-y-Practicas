#1

a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
print(f"{a} {b} {c} {d}")

#2
a, b, c = 'Coding', 'For' , 'All'
print(f"{a} {b} {c}")

#3
company = "Coding For All"

#4
print(company)

#5
print(len(company))

#6
company = company.upper()
print(company)

#7
company = company.lower()
print(company)

#8
company = company.capitalize()
print(company)

company = company.title()
print(company)

company = company.swapcase()
print(company)

company = company.swapcase()
print(company)

#9
company = company[6:]
print(company)

#10

'Index'
company = "Coding For All"
index_company = "Coding"

try:
    result = company.index(index_company)
    print(f"Tiene la palabra {index_company}")
except:
    print(f"No tiene la palabra {index_company}")

'Find'
company = "Coding For All"
palabra = "Coding"
find_company = company.find(palabra)
print(find_company)

if find_company != -1:
    print("La cadena company incluye la palabra Coding")
else:
    print("La cadena company no tiene la palabra Coding")

#11
company = "Coding For All"
c11 = company.replace("Coding", "Python")
print(c11)

#12
company = "Python For Everyone"
c12 = company.replace("Everyone", "All")
print(c12)

#13
company = "Coding For All"
c13 = company.split()
print(c13)

#14
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
c14 = company.split()
print(c14)

#15
company = "Coding For All"
c15 = company[0]
print(c15)


#16
company = "Coding For All"
c16 = len(company) - 1
print(c16)

#17
company = "Coding For All"
c17 = company[10] + "Es espacio"
print(c17)

#18
company = "Coding For All"
company = company.title()
c18 = company.split()
acronimo1 = [letra[0] for letra in c18]
acronimo2 = "".join([letra[0] for letra in c18])

print(acronimo1)
print(acronimo2)

#19
company = "Python For Everyone"
company = company.title()
c19 = company.split()
acronimo1 = [letra[0] for letra in c19]
acronimo2 = "".join([letra[0] for letra in c19])

print(acronimo1)
print(acronimo2)

#20
company = "Coding For All"
c20 = company.index("C")
print(c20)

#21
company = "Coding For All"
c21 = company.index("F")
print(c21)

#22
company = "Coding For All"
c22 = company.find("l")
print(c22)

company = "Coding For All"
c22 = company.rfind("l")
print(c22)

#23
company = 'You cannot end a sentence with because because because is a conjunction'
c23 = company.index("because")
print(f"La primera letra de la primera palabra because se encuentra en la posicion {c23}")
print("")

#24
company = 'You cannot end a sentence with because because because is a conjunction'
c24 = company.rindex("because")
print(f"La primera letra de la ultima palabra because se encuentra en la posicion {c24}")
print("")

#25
company = 'You cannot end a sentence with because because because is a conjunction'
c24 = company[31:55]
print(c24)
print("")

#26
sentence = 'You cannot end a sentence with because because because is a conjunction'
c26 = sentence.index("because")
print(f"La primera letra de la primera palabra because se encuentra en la posicion {c26}")
print("")

#27
sentence = 'You cannot end a sentence with because because because is a conjunction'
c27 = sentence[31:55]
print(c27)
print("")

#28
sentence = 'Coding For All'
c28 = sentence.startswith("Coding")
print(c28)
print("")

#29
sentence = 'Coding For All'
c29 = sentence.endswith("coding")
print(c29)
print("")

#30

sentence = '   Coding For All      '
c30 = sentence[3:17]
print(c30)
print("")

sentence = '   Coding For All      '
c30 = sentence.strip(" ")
print(c30)
print("")

#31
c31_a, c31_b = "30DaysOfPython", "thirty_days_of_python"
print(c31_a.isidentifier())
print(c31_b.isidentifier())

#32
list_32 =   ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
c32 = " # ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
print(c32)

#33
c33 = "I am enjoying this challenge.\nI just wonder what is next."
print(c33)

#34
c34 = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(c34)

#35
radius = 10
pi= 3.14
t_radius = f"radius = {int(10)}"
t_area = f"area = {float(pi)} * radius ** {int(2)}"
c35 = f"{t_radius}\n{t_area}\nEl area del circulo con radio {radius} es {int(pi * radius **2)} metros cuadrados"
print(c35)

#36
a, b = 8, 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")