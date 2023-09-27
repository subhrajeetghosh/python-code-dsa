#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

class A:
    def parenting(self):
        print("Class A : I am Parent")


class B(A):  # single level inheritance
    def children(self):
        print("Class B : I am Children")


class C(B):  # multi level inheritance
    def grand_children(self):
        print("Class C : I am Grandchildren")


b1 = B()
b1.parenting()
b1.children()

c1 = C()
c1.parenting()
c1.children()
c1.grand_children()


# python support multiple inheritence

class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")


class D(B, C):
    pass


d = D()
d.method()  # Output: "B"
print(D.mro())  # Method resolution order
super(C, d).method()  # will print "A"
