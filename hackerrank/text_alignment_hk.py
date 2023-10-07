#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
width = 20
print("hackerRank".ljust(width, "-"))
print("hackerRank".center(width, "-"))
print("hackerRank".rjust(width, "-"))
"""

thick = int(input())
char = 'H'

# first traingle
for i in (range(1, thick * 2, 2)):
    x = i * char
    print(x.center(thick * 2))

# top pillar
for i in range(thick + 1):
    x = thick * char
    print(x.rjust(thick + (thick // 2), ' ') + x.rjust(thick * 4, ' '))

# center belt
for i in range(0, thick, 2):
    x = thick * 5 * char
    print(x.rjust(thick * 5 + (thick // 2)))

# bottom pillar
for i in range(thick + 1):
    x = thick * char
    print(x.rjust(thick + (thick // 2), ' ') + x.rjust(thick * 4, ' '))

# last reversed cone
for i in reversed((range(1, thick * 2, 2))):
    x = i * char
    y = x.center(thick * 2)
    print(y.rjust(thick * 6))


def print_hackerrank_logo(thickness_1):
    c_1 = 'H'

    # Top Cone
    for i_1 in range(thickness_1):
        print((c_1 * i_1).rjust(thickness_1 - 1) + c_1 + (c_1 * i_1).ljust(thickness_1 - 1))

    # Top Pillars
    for i_1 in range(thickness_1 + 1):
        print((c_1 * thickness_1).center(thickness_1 * 2) + (c_1 * thickness_1).center(thickness_1 * 6))

    # Middle Belt
    for i_1 in range((thickness_1 + 1) // 2):
        print((c_1 * thickness_1 * 5).center(thickness_1 * 6))

    # Bottom Pillars
    for i_1 in range(thickness_1 + 1):
        print((c_1 * thickness_1).center(thickness_1 * 2) + (c_1 * thickness_1).center(thickness_1 * 6))

    # Bottom Cone
    for i_1 in range(thickness_1):
        print(((c_1 * (thickness_1 - i_1 - 1)).rjust(thickness_1) + c_1 + (c_1 * (thickness_1 - i_1 - 1)).ljust(thickness_1)).rjust(thickness_1 * 6))

if __name__ == '__main__':
    thickness = int(input())
    print_hackerrank_logo(thickness)

"""

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6))
