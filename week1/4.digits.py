# x_int = int(input("Input x: \n"))
x_int = 123456
# remember to convert to an int
first_three = x_int // 1000
last_two = x_int % 100

A = (x_int // 100) % 100




print("original input:", x_int)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", A)