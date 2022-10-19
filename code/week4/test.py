import math






EPSILON = 0.0000001


# def e(): 
#     ''' Docstring ''' 
#     e = 1
#     N = 0
#     while True:
#         if 1/math.factorial(N) > EPSILON:
#             e += 1/math.factorial(N)
#             N += 1
#         else:
#             e=round(e,10)
#             break
#     return e

def pi():
    ''' Docstring ''' 
    pi = 0
    for N in range(200000):
        if (((-1)**N / ((2*N)+1) > EPSILON)):
            pi += ((-1)**N/((2*N)+1))
        else:
            pi *= 4
            return round(pi, 10) 


print(pi())
# e shoudl be  2.7182818011