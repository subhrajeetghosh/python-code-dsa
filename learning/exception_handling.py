#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# exception that event occured during the excution that inturupt the flow of a program

try:
    numerator = int(input("Enter Numerator: "))
    denominator = int(input("Enter Denominator: "))
    result = int(numerator / denominator)
except ZeroDivisionError as z:
    print(z, "error")
except ValueError as v:
    print(v, "error")
except Exception as e:
    print("Something went wrong with error", e)
else:
    print(result)
finally:
    print("this will execute at the end!!")
