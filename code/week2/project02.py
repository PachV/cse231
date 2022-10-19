import math

BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)\n" 
 


# PROMPT = '''\nWould you like to continue (A/B)? \n'''
# "\nCustomer code (BD, D, W): \n"
# "\nNumber of days: \n"
# "Odometer reading at the start: \n"
# "Odometer reading at the end:   \n"
# "\n\t*** Invalid customer code. Try again. ***"
# "\nCustomer summary:"
# "\tclassification code:"
# "\trental period (days):"
# "\todometer reading at start:"
# "\todometer reading at end:  "
# "\tnumber of miles driven: "
# "\tamount due: $"

#  1 dial is .1 miles, 10 dial is 1 mile

print(BANNER)
contin = input("Would you like to continue (A/B)? \n")
while contin == "A":
    code = input("\nCustomer code (BD, D, W): ")


    if code == "BD":
        num_days = int(input("\nNumber of days: "))
        ord_start = int(input("\nOdometer reading at the start: "))
        ord_end = int(input("\nOdometer reading at the end:   \n"))
        
        if ord_start > ord_end:
            miles = ord_start-ord_end
            miles -= 1000000
            miles /=10
            miles = abs(miles)
        else:
            miles = (ord_end-ord_start)/10
        
        total = float(40*num_days)
        total += (miles * .25)

        print("\nCustomer summary:")
        print("\tclassification code:", code)
        print("\trental period (days):", num_days)
        print("\todometer reading at start:", ord_start)
        print("\todometer reading at end:  ", ord_end)
        print("\tnumber of miles driven: ", miles)
        print("\tamount due: $", total)

        contin = input("\nWould you like to continue (A/B)? \n" )
        if contin == "B":
            break
        else: 
            pass
    elif code == "D": #daily
        num_days = int(input("\nNumber of days: "))
        ord_start = int(input("\nOdometer reading at the start: "))
        ord_end = int(input("\nOdometer reading at the end:   "))
        
        if ord_start > ord_end:
            miles = ord_start-ord_end
            miles -= 1000000
            miles /=10
            miles = abs(miles)
        else:
            miles = abs((ord_end-ord_start)/10)

        total = float(60*num_days)
        average = miles/num_days
        if average >100:
            total += ((average-100)*.25*num_days) # the -100 is the total over number, then 25C per day
                                                  # and num_days is each day over the limit per average
        print("\nCustomer summary:")
        print("\tclassification code:", code)
        print("\trental period (days):", num_days)
        print("\todometer reading at start:", ord_start)
        print("\todometer reading at end:  ", ord_end)
        print("\tnumber of miles driven: ", miles)
        print("\tamount due: $", total)

        contin = input("Would you like to continue (A/B)? ")
        if contin == "B":
            break
        else: 
            pass
    elif code == "W":
        num_days = int(input("\nNumber of days: "))
        ord_start = int(input("\nOdometer reading at the start: "))
        ord_end = int(input("\nOdometer reading at the end:  "))
        
        if ord_start > ord_end:
            miles = ord_start-ord_end
            miles -= 1000000
            miles /=10
            miles = abs(miles)
        else:
            miles = abs((ord_end-ord_start)/10)

        weeks = math.ceil(num_days/7)
        average = miles/weeks

        if average > 900 and average < 1500:
            base = float(190*weeks)
            milage_fee = 100*weeks
            total = base + milage_fee
        elif average > 1500:
            base = float(190*weeks)
            milage_fee = 200*weeks
            extra_charge = ((average-1500) * .25) * weeks
            total = base+ milage_fee + extra_charge
        else:   # 900 or less miles on average 
            base = float(190*weeks)
            total = base

        print("\nCustomer summary:")
        print("\tClassification code:", code)
        print("\trental period (days):", num_days)
        print("\todometer reading at start:", ord_start)
        print("\todometer reading at end:  ", ord_end)
        print("\tnumber of miles driven: ", miles)
        print("\tamount due: $", total)

        contin = input("\nWould you like to continue (A/B)? \n")
        if contin == "B":
            break
        else: 
            pass
    else: 
        print("\n	*** Invalid customer code. Try again. ***")
if contin == "B":
    print("Thank you for your loyalty.")