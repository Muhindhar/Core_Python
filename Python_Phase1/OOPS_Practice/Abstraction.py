from abc import ABC, abstractmethod
class animals:
    @abstractmethod
    def makesound(self):
        pass
class dog(animals):
    def makesound(self):
        return "Woooooofff!"
class cat(animals):
    def makesound(self):
        return "meow!"
    def printsound(Animal:animals):
        print(Animal.makesound())

Dog = dog()
Cat = cat()
print("Animal sound of dog : ",Dog.makesound())
print("Cat sound : ",Cat.makesound())