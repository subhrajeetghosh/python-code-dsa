#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

class School:
    name = "Chandrakona Jirat High School"

    @classmethod
    def info(cls):
        return cls.name

    @staticmethod
    def print_info():
        print("This is a static method!")


print(School.info())
School.print_info()