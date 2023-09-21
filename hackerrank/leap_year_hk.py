#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def is_leap(year_check):
    leap = False
    if year_check % 400 == 0 or (year_check % 4 == 0 and year_check % 100 != 0):
        leap = True

    return leap


year = int(input())
print(is_leap(year))
