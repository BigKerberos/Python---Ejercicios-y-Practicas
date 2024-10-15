
class Person:
    def __init__(self,name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"# Propiedad publica
        self._name = name # Propiedad privada
        self._surname = surname



    def walk (self):
        print(f"{self._name} esta caminando")

my_person = Person("Brias", "Moure")
print(my_person._name)
my_person._name = "Steve"
print(my_person._name)
my_person.walk()
