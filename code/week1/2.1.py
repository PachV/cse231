total = 0
while True:
    num_int = int(input("Input an int: \n"))
    if num_int == 10:
        break
    else:
        total = num_int + total
print(total)
