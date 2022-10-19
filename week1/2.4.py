n_str = input("Input an int: \n")
n_int = int(n_str)

for i in range(1, n_int):
    if n_int % i == 0:
        print(i)
