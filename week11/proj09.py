# https://www.cse.msu.edu/~cse231/Online/Projects/Project09/Project09.pdf
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
    '''Docstring'''
    prices_file = input("\nEnter the price's filename: ")
    security_file = input("\nEnter the security's filename: ")
    prices_fp = open(f"{prices_file}","r", encoding="utf-8")
    security_fp = open(f"{security_file}","r")
    return prices_fp, security_fp


###############
    # prices_fp = open("small_prices.csv","r", encoding="utf-8")
    # securities_fp = open("small_securities.csv","r")
    # return prices_fp, securities_fp
###############3
    

def read_file(securities_fp):
    '''Docstring'''
    csvreader = csv.reader(securities_fp)
    header = next(csvreader)
    # print(header)
    the_set = set()
    the_dict = dict()

    for i in csvreader:
        new_key = i[0]
        new_values = i[1:-1]
        new_values.remove("reports")
        new_values.append([])
        the_dict[new_key] = new_values
        the_set.add(i[1])
    return the_set, the_dict

def add_prices (master_dictionary, prices_file_pointer):
    '''Docstring'''

    csvreader = csv.reader(prices_file_pointer)
    header = next(csvreader)
    for i in csvreader:
        new_key = i.pop(1)
        new_value = i
        # print({new_key: new_value})
        tmp_float = [float(x) for x in new_value[1:5]]
        tmp_float.insert(0,new_value[0])

        try:
            master_dictionary[new_key][-1].append(tmp_float)
        except KeyError:
            continue


def get_max_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    try:
        the_values = master_dictionary[company_symbol]
    except KeyError:
        return (None, None)
    # print(the_values[-1])
    highs = []
    for strs in the_values[-1]:
        # print(str, count)
        highs.append(strs[-1])
    try:
        maxium = max(highs)
    except ValueError:
        return 0,0
    # print(maxium)
    index_in_index = highs.index(maxium)
    date = the_values[-1][index_in_index][0]
    return (maxium, date)


def find_max_company_price (master_dictionary):
    '''Docstring'''
    highs = {}
    for company in master_dictionary:
        company_values = master_dictionary[company]
        for stat in company_values[-1]:
            highs[stat[-1]]= company
    maxium = (max(highs))
    name = highs[maxium]
    return(name, maxium)


def get_avg_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    try:
        the_values = master_dictionary[company_symbol]
    except KeyError:
        return 0.0
    # print(the_values[-1])
    highs = []
    for strs in the_values[-1]:
        # print(str, count)
        highs.append(strs[-1])
    avged =(sum(highs)/len(highs))
    return round(avged,2)


            
def display_list (lst):  # "{:^35s}"
    '''Docstring'''
    for i in range(0,len(lst),3):
        tmp_str = f"{lst[i]:^35s}{lst[i+1]:^35s}{lst[i+2]:^35s}"
        print(tmp_str)
    print("\n")

    


    
def main():
###########
    # price_fp, securties_fp = open_file()
    # the_set, the_dict =read_file(securties_fp)

    # add_prices(the_dict,price_fp)
    # # get_max_price_of_company(the_dict)
    # # find_max_company_price(the_dict)
    # get_avg_price_of_company(the_dict)

##############
    print(WELCOME)
    price_fp, securties_fp = open_file()
    the_set, the_dict =read_file(securties_fp)
    add_prices(the_dict,price_fp)

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
                        symbol = input("\nEnter company symbol for max price: ")
                        max_price, time= get_max_price_of_company(the_dict, symbol)
                        if max_price == None and time == None:
                            print("\nError: not a company symbol. Please try again.")
                            continue
                            
                        
                        elif max_price == 0 and time == 0:
                            print("\nThere were no prices.")
                            break
                        else:
                            print(f"\nThe maximum stock price was ${max_price:.2f} on the date {time}/\n")
                            break
            except EOFError:
                break
                


        if optionz == "4":
            name = find_max_company_price(the_dict)
            print(f"\nThe company with the highest stock price is MMM with a value of ${name[1]:.2f}\n")
            continue

        if optionz == "5":
            try:
                while True:
                    symbol = input("\nEnter company symbol for average price: ")
                    result =get_avg_price_of_company(the_dict,symbol)
                    if result == 0.0:
                        print("\nError: not a company symbol. Please try again.")
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
