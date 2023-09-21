#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# list use to store multiple item in single variable

car = ["farrari", "audi", "bmw", "suzuki"]
print(car)
car[0] = "tata"
print(car)
car.append("tesla")
print(car)
car.remove("tata")
print(car)
car.pop()
print(car)
car.insert(0, "ram")
print(car)
car.sort()
print(car)
car.clear()
print(car)


# 2D list

list2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8]]
print(list2d[1][2])  # will print 6

list1 = ["helllo", "hola"]
list2 = ["google", "facebook"]
main_list = [list1, list2]
print(main_list[0][1])  # will print hola
