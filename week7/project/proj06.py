#https://www.cse.msu.edu/~cse231/Online/Projects/Project06/
    
import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    '''Docstring'''
    while True:
        to_open = input("Enter file name: ")
        if to_open == "data_small" or to_open == "data":
            return open(f"{to_open}.csv", "r")

        else:
            print("uhhh no man no file do r you`")
            continue

def read_file(fp) -> tuple: # tuples version
    '''Docstring'''
    output = []
    fp.readline()
    for i in fp:
        i = i.strip().split(",")
        
        cara, rar, ele,wea,reg = i
        if reg == "":
            reg = None
        rar = int(rar)

        new_list = [cara, ele, wea,rar,reg]

        new_list = tuple(new_list)
        output.append(new_list)
    return output


def read_to_list(fp) -> list: # lists version just in case
    first_line = fp.readline()
    output = []
    for i in fp:
        i = i.strip().split(",")
        
        cara, rar, ele,wea,reg = i
        if reg == "":
            reg = None
        rar = int(rar)

        new_list = [cara, ele, wea,rar,reg]
        output.append(new_list)
    return output



def get_characters_by_criterion(list_of_tuples: list, criteria: str or int, value: str or int) -> list: # 2
    '''Docstring'''
    # print(list_of_tuples)
    match = []
    criteria1 = int(criteria)
    for i in range(len(list_of_tuples)):
        _ ,ele,wea,rar,reg = list_of_tuples[i]
        tmp_list = [_ ,ele,wea,rar,reg]

        if criteria1 == 3: # if looking for rareity
            value = int(value)
            if tmp_list[criteria1] == value:
                match.append(tmp_list)

        else: # everything else
            if tmp_list[criteria1] == None:
                tmp_list[criteria1] = "N/A"
            if tmp_list[criteria1].lower() == value.lower():
                match.append(tmp_list)


    return(match)






def get_region_list(master_list) -> list:
    '''Docstring'''
    regions = []
    for i in range(len(master_list)):
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
    '''Docstring'''
    cleaned = []
    for i in range(len(list_of_tuples)):
        _ ,ele,wea,rar,reg = list_of_tuples[i]
        tmp_list = [_ ,ele,wea,rar,reg]
        cleaned.append(tmp_list)
    sotred_clean = sorted(cleaned, key=itemgetter(0))
    sorted_clean = sorted(sotred_clean, key=itemgetter(3),reverse=True)
    return sorted_clean

def display_characters(list_of_tuples):
    '''Docstring'''
    print("{:20s}{:10s}{:10s}{:<10s}{:25s}".format("Character", "Element", "Weapon","Rarity", "Region"))
    for i in range(len(list_of_tuples)):
        char,ele,wea,rar,reg = list_of_tuples[i]
        if reg == None:
            reg = "N/A"
        print(f"{char:20s}{ele:10s}{wea:10s}{rar:<10d}{reg:25s}") 
    

def get_option():
    '''Docstring'''
    print(MENU)
    optionz = input("")
    return optionz

def get_characters_by_criteria(master_list: tuple, element: str, weapon: str, rarity:int): #3
    '''Docstring'''

    match = []
    for i in master_list:
        # print(i)
        if i[1].lower() == element.lower():
            if i[2].lower() == weapon.lower():
                if i[3] == rarity:
                    match.append(i)
    return match




    





def main():
    file_pointer = open_file()
    bad_list_of_tuples = read_file(file_pointer)

    usr_option = get_option()
    # print(list_of_tuples)
    list_of_tuples = sort_characters(bad_list_of_tuples)

    if usr_option == "1":
        print("\nRegions:")
        print(get_region_list(list_of_tuples))

    elif usr_option == "2":
        criteria = input(CRITERIA_INPUT)
        value = input("Enter value: ")
        rtrn_criteria = get_characters_by_criterion(list_of_tuples, criteria, value)
        display_characters(rtrn_criteria)

    
    elif usr_option == "3":
        element = input("Enter element: ")
        weapon = input("Enter weapon: ")
        rarity = int(input("Enter rarity "))
        returned = get_characters_by_criteria(list_of_tuples, element, weapon, rarity)
        display_characters(returned)

        
    






# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()