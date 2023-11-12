#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def print_rangoli(size):
    main_len = 4 * size - 3
    list_alpha = [chr(i) for i in range(97, 97 + size)]
    rev_list_alpha = list(reversed(list_alpha))
    for i in range(size):
        main_str = rev_list_alpha[:i + 1] + list_alpha[size - i:]
        join_str = "-".join(main_str)
        print(join_str.center(main_len, "-"))
    for i in range(size - 2, -1, -1):
        main_str = rev_list_alpha[:i+1] + list_alpha[size-i:]
        join_str = "-".join(main_str)
        print(join_str.center(main_len, "-"))

def somethign():
    print("piri")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
