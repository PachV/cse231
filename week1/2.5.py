m = int(input("Input the first integer: \n"))
n = int(input("Input the second integer: \n"))
# want the largest so end of range - 1 until % = 0
#  or smallest of the int/2 then start -1 for more efficeint 
# input 15 --> 3

if m < n:
    smaller = m
    larger = n
else:
    larger = m
    smaller= n

last = 0
for i in range(1,smaller):
    if n % i == 0:
        if m % i ==0:
            if last < i:
                last = i
                biggest = i
print(last)




# for i in range((smaller//2)+1, 0, -1):
#     if n % i == 0 and m % i == 0:
#         print(i)
#         break