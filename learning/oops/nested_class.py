#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

class Student:
    def __init__(self, name, laptop_name):
        self.name = name
        self.lap = self.Laptop(laptop_name)

    def show(self):
        print(f"Student Name : {self.name}")
        self.lap.show()

    class Laptop:
        def __init__(self, laptop_name):
            self.laptop_name = laptop_name

        def show(self):
            print(f"laptop Name : {self.laptop_name}")


s1 = Student("Leso", "Hp")
s2 = Student("hisb", "Dell")

s1.show()

l1 = s1.lap
l2 = s2.lap
l2.show()

# you can create the inner class object inside the outer class,
#                           or
# you can create object of inner class outside the outer class provided you use outer class name to call it
