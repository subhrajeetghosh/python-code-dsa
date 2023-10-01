#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

if __name__ == '__main__':
    s = input()
    is_al_num = False
    has_alpha = False
    has_digit = False
    has_lowercase = False
    has_uppercase = False
    for i in s:
        if not is_al_num and i.isalnum():
            is_al_num = True
        if not has_alpha and i.isalpha():
            has_alpha = True
        if not has_digit and i.isdigit():
            has_digit = True
        if not has_lowercase and i.islower():
            has_lowercase = True
        if not has_uppercase and i.isupper():
            has_uppercase = True
    print(is_al_num)
    print(has_alpha)
    print(has_digit)
    print(has_lowercase)
    print(has_uppercase)

# second method
    s = input()
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
