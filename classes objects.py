#Class is a blueprint of an object
#An object is an instance of a class

class Person:
    #This are the properties of a class/attriutes/variables/characteristics
    name = "james"
    age = 45
    gender = "male"


    #Methods/functions/Behaviour
    def move(self):
        print("Person is walking")

farmer = Person()
farmer.move()

print(farmer.gender)