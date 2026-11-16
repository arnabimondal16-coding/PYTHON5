class parrot:

    species = "BIRD"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu= parrot("BLU",10)
woo= parrot("WOO", 15)

print("BLU IS A {}" .format(blu.species))
print("WOO IS ALSO A {}" .format(woo.species))

print("{} is {} years old" .format(blu.name,blu.age))
print("{} is {} years old" .format(woo.name,woo.age))