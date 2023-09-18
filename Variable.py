# variable = a container for a value
first_name = "Subhrajeet"
last_name = "Ghosh"
full_name = first_name + " " + last_name
print(type(full_name))  # datatype of variable
print("Hello " + full_name)

age = 21
age += 1
print(type(age))
print(age)
print("Hello your age : " + str(age))  # cannot directly print by using '+' sign we have to cast it to String

# float datatype a numeric value that includes a decimal portion
height = 250.5
print(type(height))
print(height)
print("your height : " + str(height))  # same as the above typecasting

# Boolean value
human = True
print(type(human))
print(human)
print("are you a human? : " + str(human))  # same as the above typecasting

# Multiple assignment :
# allows us to assign multiple variable at the same time with different values
college, student, course = "New Tech College", 20, "CS"
print(college + "  Student : " + str(student) + " Course : " + course)

# allows us to assign multiple variable at the same time with same values
sohel = ranjit = pholu = john = "30"
print(sohel + ranjit + pholu + john)
