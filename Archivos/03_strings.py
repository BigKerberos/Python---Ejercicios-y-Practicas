### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea" #\n
print(my_new_line_string)

my_tab_line_string = "\tEste es un string con tabulacion" #\t
print(my_tab_line_string)

my_scape_line_string = "\\tEste es un string\\nescapado" #\\t \\n ignora el \
print(my_scape_line_string)

# Formateo

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
print("")
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

#Division
print("")
language_slice = language[0:4]
print(language_slice)

language_slice = language[0:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6]
print(language_slice)

# Reverse
print("")

reverse_language = language[::-1]
print(reverse_language)

# Funciones
print("")
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))