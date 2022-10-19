# secs_str = input("Input seconds: \n") # do not change this line
secs_int = 80000
hours = secs_int // 3600
minutes = (secs_int - hours * 3600) // 60
seconds = secs_int - (hours * 3600) - (minutes * 60)
print(hours,":",minutes,":",seconds) # do not change this line