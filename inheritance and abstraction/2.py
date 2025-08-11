from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can walk and bark")

class Lion(Animal):
    def move(self):
        print("I can walk and roar")

ob = Human()
ob.move()

ob1= Snake()
ob1.move()

ob2 = Dog()
ob2.move()

ob3= Lion()
ob3.move()

