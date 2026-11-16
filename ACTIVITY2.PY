class student:
    grade = 10
    name = "PENGUIN"

    def introduction(self):
        print("HI! I AM A STUDENT")

    def details(self):
        print("MY NAME IS ", self.name)
        print("I STUDY IN GRADE ", self.grade)

ob = student()
ob.introduction()
ob.details()