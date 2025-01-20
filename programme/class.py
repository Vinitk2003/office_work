# class Dog:
#     species = "Canine" # class Attribute
#     surname = "patel"

#     def __init__(self, name, age):
#         self.name = name #instance attribute
#         self.age = age #instance attribute

# print(Dog.species)
# print(Dog.surname) 

# dog1 = Dog("Buddy", 10)


# print(dog1.age)
# print(dog1.name)
        
#class and objects
class Dog: #defining class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")
#creating instance of the Dog class
dog1 = Dog("Buddy", 10)
dog2 = Dog("Max", 20)

#accssing instance attributes and calling methods
dog1.bark()
print(f"{dog1.name} is {dog1.age} years old")