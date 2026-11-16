class parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, sing):
        return "{} sings {}" .format(self.name,sing)

    def dance(self):
        return "{} is now dancing".format(self.name)

blu = parrot("BLU",10)


print(blu.sing("'HAPPY'"))
print(blu.dance())