#1
dog = {}
print(type(dog))

#2
dog = {"Name":"Roy", "Color":"White", "Breed":"Pixie bob", "Legs":3, "Age":1}
print(dog)

#3
student = {"first_name":"Brandon", "last_name":"Lagunas", "gender":"Masculino", "age":25, "marital status":"Single", "skills":["Python", "HTML"], "country":"México", "city":"Zapopan", "address":"Av Vallarta 5846"}

#4
print(len(student))

#5
print(student["skills"])
print(type(student["skills"]))

#6
student["skills"].append("Office")
student["skills"].insert(1,"C+")
print(student["skills"])

#7
stdt_keys = list(student.keys())
print(stdt_keys)

#8
stdt_values = list(student.values())
print(stdt_values)

#9
stdt_tuples = student.items()
print(stdt_tuples)

#10
del student["marital status"]
print(student)

#11
del student
'print(student)' #Error