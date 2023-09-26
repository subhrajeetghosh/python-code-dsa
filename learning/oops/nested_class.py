#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

class Student:
    def __init__(self, name):
        self.name = name
        self.lap = self.Laptop()

    class Laptop:
        def __init__(self):
            self.laptop_name = "Dell"


s1 = Student("Leso")
s2 = Student("hisb")

l1 = s1.lap
l2 = s2.lap

# you can create the inner class object inside the outer class,
#                           or
# you can create object of inner class outside the outer class provided you use outer class name to call it
