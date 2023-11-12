#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
from collections import Counter

number_shoes = int(input())
input_string = input()
my_list = [int(x) for x in input_string.split()]
map_shoe = dict(Counter(my_list))
number_customer = int(input())
total_sell_amount = 0
for i in range(number_customer):
    shoe_size, current_price = map(int, input().split())
    if shoe_size in map_shoe and map_shoe[shoe_size] > 0:
        total_sell_amount += current_price
        map_shoe[shoe_size] -= 1

print(total_sell_amount)
