################################################
# Project 04
#   Tell the user the options and ask for input
#    if does not exist, reprint the menu and ask again
#   match the input and call the function with the argument
#   function returns the value
#   print out the function value vs the math function and their differences  
#   Ask for anther option
#   if X, exit() the program
################################################


import math
EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''
def factorial(num: int) -> int:
    '''
    finds the factorial of input
    parameter is int, returns int
    linear iterative process

    ''' 
    counter = 1
    product = 1
    if int(num) < 0:
        return None
    while int(counter) <= int(num):
        product = counter * product
        counter +=1
    return product
 
def e() -> float: 
    '''
    Calculates the value of e using sums
    no parameter, and outputs float
    ''' 
    a = float(1.0)
    b = float(0.0) # behind 1 execution of (i:num)
    for i in range(1,2000):
        a += (1 / (math.factorial(i)))
        b += (1 / (math.factorial(i-1)))

        if abs(a - b) < EPSILON:
            return round(b,10)

def pi() -> float:
    '''
    find the value of pi using sums
    no parameter, outputs float
    ''' 
    combined = float(0)
    combined_beh = float(0)
    for i in range(30000000):
        combined += (((-1)**i)/((2*i)+1))

        if i < 1:
            continue
        else:
            # behind 1 i for comparison
            combined_beh += (((-1)**(i-1))/((2*(i-1))+1))

            if abs((combined_beh)- (combined)) < EPSILON:
                return round((combined_beh*4),10)

def sinh(x:float) -> float: 
    ''' 
    find value of sinh(x) using sums
    parameter is float, outputs float
     ''' 
    try:
        x_flt = float(x)
    except:
        exit()
    combined = float(0)
    combined_beh = float(0)
    for i in range(220):
        combined += ((x_flt**((2*i)+1)))/(math.factorial((2*i)+1))

        if i < 1: #if i is 0, i-1 will be -1, which wont work
            continue
        else: # behind 1 of i
            combined_beh += (x_flt**((2*(i-1))+1))/(math.factorial(2*(i-1)+1))

            if abs(combined - combined_beh) < EPSILON:
                return round(float(combined_beh),10)

def main(): 
    print(MENU)
    while True:
        option = input("\nChoose an option: ").lower()
        if option == "f":
            print("\nFactorial")
            try:
                N = int(input("Input non-negative integer N: \n"))
            except ValueError:
                print("Invalid N.")
                continue
            if N < 0:
                print("Invalid N.")
                continue
            result = factorial(N)
            print(f"Calculated: {result}\nMath: {math.factorial(N)}")
            print(f"Diff: {result-math.factorial(N)}")

        elif option =="e":
            print("\ne")
            result = e()
            print(f"Calculated: {result}\nMath: {math.e:.10f}")
            print(f"Diff: {abs(result-math.e):.10f}")
                                        #:.10f round it to 10 decimals
        elif option =="p":
            print("\npi")
            result = pi()
            print(f"Calculated: {result}\nMath: {math.pi:.10f}")
            print(f"Diff: {abs(result-math.pi):.10f}")

        elif option =="s":
            print("\nsinh")
            X = input("X in radians: ")
            try:
                X = float(X)
            except:
                print("\nInvalid X.")
                continue
        
            result = sinh(X)
            X = float(X)
            print(f"\nCalculated: {result}\nMath: {math.sinh(X):.10f}")
            print(f"Diff: {abs(result-math.sinh(X)):.10f}")

        elif option =="m":
            main()
        elif option =="x":
            print("\nThank you for playing.")
            exit()
        else:
            print(f"\nInvalid option: {option.upper()}")
            print(MENU)

    

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()

