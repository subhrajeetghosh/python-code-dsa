#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    # You can also define concrete (non-abstract) methods in the abstract class
    def common_method(self):
        print("This is a common method.")


class MyConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print("Concrete implementation of my_abstract_method.")


# Attempting to create an instance of the abstract class will result in a TypeError.
# obj = MyAbstractClass()  # This will raise an error.

# Create an instance of the concrete subclass
obj = MyConcreteClass()
obj.my_abstract_method()  # Calls the concrete implementation
obj.common_method()  # Calls the common method
