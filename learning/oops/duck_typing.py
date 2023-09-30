#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def print_animal_sound(animal):
    print(animal.sound())


class Dog:
    def sound(self):
        return "Woof!"


class Duck:
    def sound(self):
        return "Quack!"


# Both Dog and Duck have a 'sound' method, so we can use them interchangeably.
dog = Dog()
duck = Duck()

print_animal_sound(dog)  # Output: "Woof!"
print_animal_sound(duck)  # Output: "Quack!"
