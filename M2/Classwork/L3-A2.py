class student:
    grade = 10
    name = "penguin"


    def introduction(self):
        print ("hi i am student")

    def details(self):
        print ("my name is", self.name)
        print ("i am in grade", self.grade)

ob = student()
ob.introduction()
ob.details()


