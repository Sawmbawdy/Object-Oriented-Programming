class parrot:
    species = 'bird'
    def __init__(self, age, name):
        self.age = age
        self.name = name


Wu = parrot(10, 'Wu')
Blu = parrot(15, 'Blu')

print("The age of Blu is", Blu.age)
print("The 10 year old parrot is", Wu.name)

print("both the species are", Wu.species)