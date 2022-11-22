###############################
#   proj 09
#   ask for the price and security file name first
#   then the master dict and set will be set up, it is used to call functions
#   print out the menu and ask the user to select which function to go to
#   ask for the required stuff that is needed to call the function
#   and print out the result using display_list() or other ways 
##############################

import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''ask user for file and try to open it, if it cant, then prompt again'''
    prices_fp = None
    security_fp = None

    while True:
        prices_file = input("\nEnter the price's filename: ")
        try:
            prices_fp = open(f"{prices_file}","r")
            break
            
        except FileNotFoundError:
            print("Not found, try again.")
    
    while True:
        security_file = input("\nEnter the security's filename: ")
        try:
            security_fp = open(f"{security_file}","r")
            return prices_fp, security_fp
        except FileNotFoundError:
            print("File not found, try again")
            


def read_file(securities_fp):
    '''make a dict with the companies name as the key, and
        their info as values 
        also make a set that is the companies in securities.csv
        return the dict and set
    '''
    csvreader = csv.reader(securities_fp)
    header = next(csvreader)
    the_set = set()
    the_dict = dict()

    for i in csvreader:
        new_key = i[0]
        new_values = i[1:-1]
        new_values.remove("reports") #this index isnt used for anything
        new_values.append([])
        the_dict[new_key] = new_values
        the_set.add(i[1])
    return the_set, the_dict

def add_prices (master_dictionary, prices_file_pointer):
    '''each value in the key, add the price history at index [-1], and
        convert it into float
    '''

    csvreader = csv.reader(prices_file_pointer)
    header = next(csvreader)
    for i in csvreader:
        new_key = i.pop(1)
        new_value = i
        tmp_float = [float(x) for x in new_value[1:5]]
        tmp_float.insert(0,new_value[0])

        try:
            master_dictionary[new_key][-1].append(tmp_float)
        except KeyError:
            continue

def get_max_price_of_company (master_dictionary, company_symbol):
    '''use the parameter to find the price history fo the company
        then put all the highest value per that day into a list,
        then max() it to find the highest value
    
    '''
    try:
        the_values = master_dictionary[company_symbol]
    except KeyError:
        return (None, None)
    highs = []
    for strs in the_values[-1]:
        highs.append(strs[-1])
    try:
        maxium = max(highs)
    except ValueError:
        return 0,0

    # 0 index is first high price, 1th index is the 2nd high price
    index_in_index = highs.index(maxium)
    date = the_values[-1][index_in_index][0]
    return (maxium, date)

def find_max_company_price (master_dictionary):
    '''make a dict, the key is the price, and the value is company symbol
        use the max() to find max price, and use the key to find the symbol
    '''
    highs = {}
    for company in master_dictionary:
        company_values = master_dictionary[company]
        for stat in company_values[-1]:
            highs[stat[-1]]= company
    maxium = (max(highs))
    name = highs[maxium]
    return(name, maxium)

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''same as get max price of company
        but we find the average of them with sum() and len() 
    '''
    try:
        the_values = master_dictionary[company_symbol]
    except KeyError:
        return 0.0
    highs = []
    for strs in the_values[-1]:
        highs.append(strs[-1])
    avged =(sum(highs)/len(highs))
    return round(avged,2)
            
def display_list (lst):
    '''remin_len is the last row that needed to be formatted
        each interation will skip 3 numbers, and use
        math to find out the missing numbers, then index them using `[i]`
    '''
    remin_len = len(lst) % 3
    for i in range(0,len(lst),3):
        try:
            tmp_str = f"{lst[i]:^35s}{lst[i+1]:^35s}{lst[i+2]:^35s}"
            print(tmp_str)
        except IndexError:
            # left overs
            if remin_len == 1: 
                print(f"{lst[len(lst)-1]:^35s}",end="")
            elif remin_len == 2:
                print(f"{lst[len(lst)-1]:^35s}{lst[len(lst)-2]:^35s}",end="")
            elif remin_len == 3:
                print(f"{lst[len(lst)-1]:^35s}{lst[len(lst)-2]:^35s}\
                    {lst[len(lst)-3]:^35s}",end="")
            else:
                print("how???????????")
    print("\n")

def main():
    print(WELCOME)
    price_fp, securties_fp = open_file()
    the_set, the_dict =read_file(securties_fp)
    add_prices(the_dict,price_fp)
    price_fp.close()
    securties_fp.close()

    optionz = 0

    while optionz !=6:
        optionz = input(MENU +"\n\nOption: ")

        if optionz == "1":
            title = "Companies in the New York Stock Market from 2010 to 2016"

            print(f"\n{title:^105s}")
            the_list = list(the_set)
            the_list.sort()

            display_list(the_list)
            continue
        if optionz == "2":
            print("\ncompanies' symbols:")
            the_list = (list(the_dict.keys()))
            the_list.sort()
            display_list(the_list)

        if optionz == "3":
            try:
                while True:
                        symbol = input("\nEnter company symbol for\
 max price: ")
                        max_price, time= get_max_price_of_company\
                            (the_dict, symbol)
                        if max_price == None and time == None:
                            print("\nError: not a company symbol.\
 Please try again.")
                            continue
                            
                        elif max_price == 0 and time == 0:
                            print("\nThere were no prices.")
                            break
                        else:
                            print(f"\nThe maximum stock price was \
${max_price:.2f} on the date {time}/\n")
                            break
            except EOFError:
                break

        if optionz == "4":
            name = find_max_company_price(the_dict)
            print(f"\nThe company with the highest stock price is \
{name[0]} with a value of ${name[1]:.2f}\n")
            continue

        if optionz == "5":
            try:
                while True:
                    symbol = input("\nEnter company symbol\
 for average price: ")
                    result =get_avg_price_of_company(the_dict,symbol)
                    if result == 0.0:
                        print("\nError: not a company symbol. \
Please try again.")
                        continue
                    else:
                        print(f"\nThe average stock price was ${result}.\n")
                        break
            except EOFError:
                break
            
        if optionz == "6":
            exit()
if __name__ == "__main__": 
    main() 
