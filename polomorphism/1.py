class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age=age
    
    def info(self):
        print("I am a cat. My name is",self.name,".", "I am", self.age,"years old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age=age
    
    def info(self):
        print("I am a dog. My name is", self.name, ".I am", self.age,"years old.")

    def make_sound(self):
        print("Bark")

cat = Cat("Coco", 3)
dog = Dog("Bruno", 5)

for animal in (cat, dog):
    animal.info()
    animal.make_sound()
