#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# link - https://www.lintcode.com/problem/2364

def prime_checker(number):
    if number != 2:
        currnet_div = 2
        while number / 2 >= currnet_div:
            if number % currnet_div == 0:
                return False
            else:
                currnet_div += 1
        if number / 2 > currnet_div:
            return True
    return True


num = int(input())
current_checker = 1
for i in range(num):
    current_checker += 1
    while not prime_checker(current_checker):
        current_checker += 1
print(current_checker)


