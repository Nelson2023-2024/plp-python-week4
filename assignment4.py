class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of Person
person1 = Person("John Doe", 30, "Male")

# Calling the introduce method
person1.introduce()
