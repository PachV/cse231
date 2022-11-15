# https://www.cse.msu.edu/~cse231/Online/Projects/Project08/Project08.pdf
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
    #prices_file = input("Enter the price's filename: ")
    #security_file = input("Enter the security's filename: ")
#    prices_fp = open(f"{prices_file}","r")
#    security_fp = open(f"{security_file}","r")
#    return prices_fp, security_fp


###############
    prices_fp = open("small_prices.csv","r", encoding="utf-8")
    securities_fp = open("small_securities.csv","r")
    return prices_fp, securities_fp
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
    try:
        the_values = master_dictionary[company_symbol]
    except KeyError:
        return (None, None)
    # print(the_values[-1])
    highs = []
    for strs in the_values[-1]:
        # print(str, count)
        highs.append(strs[-1])
    maxium = max(highs)
    # print(maxium)
    index_in_index = highs.index(maxium)
    date = the_values[-1][index_in_index][0]
    return (maxium, date)


def find_max_company_price (master_dictionary):
    '''Docstring'''
    pass

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    pass
            
def display_list (lst):  # "{:^35s}"
    '''Docstring'''
    pass
    
def main():
###########
    price_fp, securties_fp = open_file()
    the_set, the_dict =read_file(securties_fp)

    add_prices(the_dict,price_fp)
    print(get_max_price_of_company(the_dict))
##############





if __name__ == "__main__": 
    main() 
