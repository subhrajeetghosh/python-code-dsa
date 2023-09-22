#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

name = "Shubaa"


def display_name():
    name = "Code"  # local scope available inside function only
    print(name)


display_name()
print(name)