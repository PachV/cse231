n_str = input("Input an int: \n")
n_int = int(n_str)

total = 1
i = 0
while total <= n_int:
    i += 1
    if i % 2 != 0:
        print(i)
        total += 1


