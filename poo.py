class Animal:
    lives = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print('Hola, soy ' + self.name + 'y tengo ' + str(self.age) + 'años')

    def speak(self, sound):
        print(sound)
#--------------

a1 = Animal('Tony', 15)
a2 = Animal('Sara', 4)
a3 = Animal('Ringo', 8)

print(a1.name)
print(a2.name)
print(a3.age)

print(a1.lives)
print(a2.lives)
print(a3.lives)

a1.describe()
a2.speak('Miau')