##########################################################
# Project 01
#  Prompt asking an number
#  User inputs the number
#   Unit and math converstion with the input number
#    Converstion will be using the data type 'float'
#   Print the final result as float and round it to 3
##########################################################

rods_float = float(input("Input rods: \n"))

# KEY-----------------------------------------
# • 1 rod = 5.0292 meters
# • 1 furlong = 40 rods
# • 1 mile = 1609.34 meters
# • 1 foot = 0.3048 meters
# • average walking speed is 3.1 miles per hour
# ------------------------------------------------

# convertions

meters = rods_float * 5.0292
feet = meters * 3.280839895
miles = meters/1609.34
furlongs = rods_float/40

hour_to_min = 3.1/60
min_to_walk = (miles/hour_to_min)

# output
print("You input", round(rods_float,3),"rods.")
print("")
print("Conversions")
print("Meters:", round(meters,3))
print("Feet:", round(feet,3))
print("Miles:", round(miles,3))
print("Furlongs:", round(furlongs,3))
print("Minutes to walk", rods_float, "rods:", round(min_to_walk,3))


# Test 2
# Input rods: 10
# You input 10.0 rods.
# Conversions
# Meters: 50.292
# Feet: 165.0
# Miles: 0.031
# Furlongs: 0.25
# Minutes to walk 10.0 rods: 0.605