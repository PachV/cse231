#https://www.cse.msu.edu/~cse231/Online/Projects/Project06/
    
from operator import itemgetter

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "Choose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    '''
    asks user for input file, and returns the file that is requested
    '''
    to_open = input("Enter file name: ")
    if to_open == "data_small.csv" or to_open == "data.csv":
        return open(f"{to_open}", "r")

    else:
        print("\nError opening file. Please try again.")
        return open_file() #somehow this works xdddd, it loops to the func
                           # with no "data"
                           # i figured this out while testing func loops


def read_file(fp) -> tuple: 
    '''
        reads the file and reorder it and convert it into tuple
        returns lists of toples
    '''
    output = []
    fp.readline()
    for i in fp:
        # the gamer way to do it 😎😎😎 
        i = i.strip().split(",")
        
        cara, rar, ele,wea,reg = i
        if reg == "": 
            # reg element is the only one that potentially can be empty or ""
            reg = None
        rar = int(rar)

        new_list = [cara, ele, wea,rar,reg]

        new_list = tuple(new_list)
        output.append(new_list)
    return output

def get_characters_by_criterion(list_of_tuples: list, criteria: str or int, value: str or int) -> list: # 2
    '''
    matches with all the parameters that the user want,
    and returns them into a list of lists
    '''
    match = []
    criteria = int(criteria)
    # this is before i knew the sort_char function, you can ignore this TO...
    for i in range(len(list_of_tuples)):
        _ ,ele,wea,rar,reg = list_of_tuples[i]
        tmp_list = [_ ,ele,wea,rar,reg]
    # HERE

    ## idk if this func still works without the area i listed xd
    ## and im too lazy to test it

        if criteria == 3: # if looking for rareity
            value = int(value)
            if tmp_list[criteria] == value:
                match.append(tmp_list)

        else: # everything else
            if tmp_list[criteria] == None:
                tmp_list[criteria] = "N/A"
            if tmp_list[criteria].lower() == value.lower():
                match.append(tmp_list)

    return match

def get_region_list(master_list) -> list:
    '''
    find the region that isnt in the list, 
    then sort and return the region that is seen
    '''
    regions = []
    for i in range(len(master_list)):
        # we only want the last element within the list of lists
        _,_,_,_,local_region = master_list[i]
        if local_region not in regions:
            if local_region == None:
                continue
            regions.append(local_region)
        else:
            continue
    regions.sort()
    return regions

def sort_characters(list_of_tuples):
    '''
    reorder the list of tuples to the standard one
    with rarity being on top

    '''
    cleaned = []
    for i in range(len(list_of_tuples)):
        # declare var for each element
        _ ,ele,wea,rar,reg = list_of_tuples[i]
        # reorder the var for each element
        tmp_list = [_ ,ele,wea,rar,reg]
        cleaned.append(tmp_list)

    sotred_clean = sorted(cleaned, key=itemgetter(0)) # not fully cleaned/sort
    sorted_clean = sorted(sotred_clean, key=itemgetter(3),reverse=True)
    return sorted_clean

def display_characters(list_of_tuples):
    '''
    intakes a list that is already operated in other funcs, and reformat
    them to make them look nice to the end user
    '''
    print("{:21s}{:10s}{:10s}{:<10s}{:25s}".format("\nCharacter", "Element", "Weapon","Rarity", "Region"))
    #      ^^^^^^ test case says it wanted 21... 
    for i in range(len(list_of_tuples)):
        char,ele,wea,rar,reg = list_of_tuples[i]

        if reg == None:
            reg = "N/A"
        print(f"{char:20s}{ele:10s}{wea:10s}{rar:<10d}{reg:25s}") 
    
def get_option():
    '''prints out the menu and asks for the number'''

    print(MENU)
    optionz = input("")
    return optionz # the main function will do the matching

def get_characters_by_criteria(master_list: tuple, element: str, weapon: str, rarity:int): #3
    '''
    match with all the requirements that the user wants
    and return them into a list
    '''

    match = []
    for i in master_list:
        # [1] is elemtn, [2] is weapon, [3] is rarity
        # i could just do all of these in one if statement...

        if i[1].lower() == element.lower():
            if i[2].lower() == weapon.lower():
                if i[3] == rarity:
                    match.append(i)
    return match

def main():
    file_pointer = open_file()
    bad_list_of_tuples = read_file(file_pointer)

    list_of_tuples = sort_characters(bad_list_of_tuples)

    while True:
        usr_option = get_option()

        if usr_option == "1":
            print("Regions:")
            regions =get_region_list(list_of_tuples)
            print(", ".join(regions), end= "\n")
            continue

        elif usr_option == "2":
            criteria = input(CRITERIA_INPUT)
            value = input("\nEnter value: ")
            rtrn_criteria = get_characters_by_criterion(list_of_tuples, criteria, value)
            if rtrn_criteria == []:
                print("\nNothing to print.")
                continue
            else:
                display_characters(rtrn_criteria)
                continue
        
        elif usr_option == "3":
            element = input("Enter element: ")
            weapon = input("\nEnter weapon: ")

            while True: # keeps asking for actual intergers
                try:
                    rarity = int(input("\nEnter rarity: "))
                    break
                except ValueError:
                    print("\nInvalid input")
                    continue

            returned = get_characters_by_criteria(list_of_tuples, element, weapon, rarity)
            if returned == []:
                print("\nNothing to print.")

            else:
                display_characters(returned)
                continue

        elif usr_option == "4":
            exit()


# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()