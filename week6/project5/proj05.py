# https://www.cse.msu.edu/~cse231/Online/Projects/Project05/


import math

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262

def open_file():
    ''' opens the file as desired and return the file pointer '''
    counter = 0
    while True:
        if counter >= 1: #first time
            to_open = input("Enter a file name: ").lower()
        else:
            to_open = input("Input data to open: ").lower()

        if ((to_open == "kgf") or (to_open == "singlestar")\
             or (to_open == "small") or (to_open == "all")):
            if to_open == "kgf":
                to_open = "KGF" # the file name is capitalized
            file_pointer = open(f"{to_open}.csv","r")
            return file_pointer
        else:
            print("\nError: file not found.  Please try again.")
            counter +=1

def make_float(s:str) -> bool or float:
    ''' take in a string and trys to convert it into a float 
        if it can't, returns -1, else the parameter but in float    
        parameter is string, returns -1 or float of the string.
    '''
    try:
        s = float(s)
        return s
    except ValueError:
        return -1
  
def get_density(mass: float, radius: float) -> float:
    ''' takes in mass and radius, and return the density using math
        parameter is float, and returns float
    '''
    if radius <= 0:
        return -1

    density = 0
    mass = EARTH_MASS * mass
    radius = EARTH_RADIUS * radius

    volume = (4/3)*math.pi*radius**3
    density = mass/volume
    return density

def temp_in_range(axis:float, star_temp:float, star_radius:float,\
     albedo:float, low_bound:float, upp_bound:float) -> bool:
    ''' return the bool if planet is in the range of desired temp using math
        if any of the parameter is negative, it will return false
        parameters are all float, and returns Bool
    ''' 

    if axis < 0 or star_temp < 0 or star_radius < 0:
        return False
    
    star_radius = SOLAR_RADIUS * star_radius
    axis *= AU

    #formula for planet temp
    planet_temp = (star_temp)*((star_radius/(2*axis))**0.5)*(1-albedo)**0.25

    #if outside of the bound, it will return False
    if planet_temp < low_bound or planet_temp > upp_bound:
        return False
    return True

def get_dist_range() -> float:
    ''' Find the distance that the user want
        and make sure its a valid number
        no parameter, and returns float, it is in parsec 
    '''
    while True:
        distance = input("\nEnter maximum distance from Earth (light years): ")
        try:
            distance = float(distance)
            if distance <= 0.0:
                print("\nError: Distance needs to be greater than 0.")
                continue
        except ValueError:
            print("\nError: Distance needs to be a float.")
            continue
        return distance / PARSEC_LY # same as our .csv file distance
def main():
 
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')
    
    opened_file = open_file()
    dist_range = get_dist_range()
    opened_file.readline()

    # set init values
    low_bound = 200.0
    upp_bound = 350.0
    albedo = 0.5

    pl_name = ""
    pl_orbsmax = None
    distance = None
    pl_rade = None
    pl_bmasse = None
    st_teff = None
    st_rad = None
    
    max_star_in_system = 0
    star_in_system = 0

    max_pl_in_system = 0
    pl_in_system = 0
    
    total_pmass = 0
    count_for_weight = 0

    rocky = 0
    gassy = 0

    habitable = 0
    rocky_clost_name = None
    gasy_clost_name = None

    rock_min_distance = 99999
    gas_min_distance = 99999

    #read line by line and extract the values from it
    for i in opened_file:
        pl_name = i[:25]

        distance = i[114:]
        distance = make_float(distance) # dist is now float

        # if outside of our range, and if unknown, skip
        if distance < 0 or distance > dist_range:
            continue

        # finds max stars in system
        star_in_system = int(i[50:57])

        #find the bigger one
        if star_in_system > max_star_in_system:
            max_star_in_system = star_in_system

        # finds planets in system
        pl_in_system = int(i[58:65])

        #find the bigger one
        if pl_in_system > max_pl_in_system:
            max_pl_in_system = pl_in_system
        
        #axis
        pl_orbsmax = i[66:77]
        pl_orbsmax = make_float(pl_orbsmax)

        #planet radius
        pl_rade = i[78:85]
        pl_rade = make_float(pl_rade)
 
        #planet mass
        pl_bmasse = i[86:96]
        pl_bmasse = make_float(pl_bmasse)
        if pl_bmasse == -1: #ignores UNKNOWN
            pass
        else:
            count_for_weight += 1
            total_pmass += pl_bmasse

        #star temp
        st_teff = i[97:105]
        st_teff = make_float(st_teff)
   
        #star radius
        st_rad = i[106:113]
        st_rad = make_float(st_rad)

        density = get_density(pl_bmasse,pl_rade)
        
        if temp_in_range(pl_orbsmax,st_teff,st_rad,albedo,\
            low_bound,upp_bound,):

            habitable +=1

            #rock?
            if pl_bmasse > 0 and pl_bmasse < 10 or (pl_rade >0 and\
                 pl_rade < 1.5) or density > 2000:
                rocky +=1
                if distance <= rock_min_distance:
                    # the current is the closest
                    rock_min_distance = distance
                    rocky_clost_name = pl_name

            #gassy?
            else:
                gassy +=1
                if distance < gas_min_distance:
                    # the current is the closest
                    gas_min_distance = distance
                    gasy_clost_name = pl_name

    
    ### it will look a lot nicer if there isnt 80 character limit per line...
    #outputs
    print(f"\nNumber of stars in systems with the \
most stars: {max_star_in_system}.")

    print(f"Number of planets in systems with the \
most planets: {max_pl_in_system}.")

    print(f"Average mass of the planets: \
{total_pmass/count_for_weight:.2f} Earth masses.")

    print(f"Number of planets in circumstellar habitable zone: {habitable}.")

    rock_min_distance %= 99999 # if there is no rock, then it will be 0
    gas_min_distance %= 99999 # ^^^^^^^^^^^^^^^^^
    if rocky >0:
        print(f"Closest rocky planet in the circumstellar habitable \
zone {rocky_clost_name.strip()} is {rock_min_distance*PARSEC_LY:.2f} light \
years away.")

    else:
        print("No rocky planet in circumstellar habitable zone.")

    if gassy >0:
        print(f"Closest gaseous planet in the circumstellar habitable zone \
{gasy_clost_name.strip()} is {gas_min_distance*PARSEC_LY:.2f} \
light years away.") # * it by parsec makes it light years

    else:
        print("No gaseous planet in circumstellar habitable zone.")

if __name__ == "__main__":
    main()
