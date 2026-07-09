class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof! and it is {self.age} years old."

my_dog = Dog("Tom", 3)
my_dog2=Dog("Jerry", 5) 
print(my_dog.bark())
print(my_dog2.bark())