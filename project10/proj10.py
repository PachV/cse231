###########################################
# project 10
# setup the board with initalize()
# then print the menu and display the board
# then ask the user for a input with menu
# call parse_option() to see if its valid
# if not then printout the error
# then call the option with the user selected option
# then call check_win to see if they won
# and keep looping until the user won or exit() it
#########################################

from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    '''make the standard setup for the game
        and all the cards are flipped except the [-1]index
    '''
    tableau = [[] for _ in range(7)]
    foundation = [[],[],[],[]]
    stock = []
    waste = []
    deck = Deck()
    deck.shuffle()

    start = 0
    while True:
        for i in range(start,7):
            popped = deck.deal() # same as .pop()
            tableau[i].append(popped)
        start +=1
        if start == 7:
            break
    
    for i in range(7):
        for j in range(i):
            (tableau[i][j].flip_card())# flip everyhting except last

    stock = deck
    
    waste.append(deck.deal())
    return tableau,stock ,foundation,waste

def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''if stock is empty, return false
        if not, pop the stock and put it in waste
    '''
    if stock.is_empty():
        return False
    else:
        waste = waste.append(stock.deal())
        return True
       
def waste_to_foundation( waste, foundation, f_num):
    '''put waste into foundation,
        and check if the move is valid,
        if it is end appent it to the foundation
    '''
    waste_last = waste[-1]
    if len(foundation[f_num]) == 0:
        if waste_last.rank() != 1:
            return False
        else:
            popped=waste.pop()
            foundation[f_num].append(popped)
            return True
            
    found_last = foundation[f_num][-1]

    if waste_last.suit() == found_last.suit():
        if waste_last.rank() - found_last.rank() == 1:
            foundation[f_num].append(waste_last)
            waste.pop()
            return True

    return False

def waste_to_tableau( waste, tableau, t_num ):
    '''put waste to table,
        if the color is the same, then it cant,
        if the table - the waste card is equal to 1
        then it is a valid move
        and then pop waste
    '''
    waste_last = waste[-1]
    if len(tableau[t_num]) == 0:
        if waste_last.rank() == 13:
            tableau[t_num].append(waste_last)
            waste.pop()
            return True
        return False

    found_last = tableau[t_num][-1]

    if waste_last.suit() == found_last.suit():
        return False
    else:
        # [2,3] are red, [1,4] are black
        if 2 in (waste_last.suit(), found_last.suit()) and 3 in (waste_last.suit(), found_last.suit()):
            return False
        elif 1 in (waste_last.suit(), found_last.suit()) and 4 in (waste_last.suit(), found_last.suit()):
            return False
        else:
            if found_last.rank() - waste_last.rank() == 1:
                tableau[t_num].append(waste_last)
                waste.pop()
                return True
            return False

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''check if the move is valid, 
    if so then append to the foundation and pop the table
    then flip the card if its not face up
    '''
    if len(foundation[f_num]) == 0:
        if tableau[t_num][-1].rank() == 1:
            popped = tableau[t_num].pop()
            foundation[f_num].append(popped)
            if len(tableau[t_num]) == 0:
                return True
            if not tableau[t_num][-1].is_face_up():
                tableau[t_num][-1].flip_card()
            return True
        else:    
            return False
    if len(tableau[t_num]) == 0:
        return False

    found_last = foundation[f_num][-1]
    table_last = tableau[t_num][-1]

    if found_last.suit() == table_last.suit():
        if table_last.rank() - found_last.rank() == 1:
            t_last =tableau[t_num].pop()
            foundation[f_num].append(t_last)
            if len(tableau[t_num]) == 0:
                return True
            if not tableau[t_num][-1].is_face_up():
                tableau[t_num][-1].flip_card()

            return True
        return False
    else:
        return False

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''if both are the same color, its invalid,
        if the t_num2 - t_num 1 = 1
        then it is a valid move
        then check if the t_num1's previous card is faced up
        if not then make it face up
    '''
    if len(tableau[t_num2]) == 0:
        if tableau[t_num1][-1].rank() == 13:
            popped = tableau[t_num1].pop()    
            tableau[t_num2].append(popped)
            if not tableau[t_num1][-1].is_face_up():
                tableau[t_num1][-1].flip_card()
            return True
        return False

    n1 = tableau[t_num1][-1]
    n2 = tableau[t_num2][-1]

    if n1.rank() == n2.rank():
        return False

    if 2 in(n1.suit(), n2.suit()) and 3 in (n1.suit(), n2.suit()):
        return False
    if 1 in(n1.suit(), n2.suit()) and 4 in (n1.suit(), n2.suit()):
        return False
    
    if n2.rank() - n1.rank() == 1:
        popped = tableau[t_num1].pop()
        tableau[t_num2].append(popped)
        if len(tableau[t_num1]) == 0:
            return True
        if not tableau[t_num1][-1].is_face_up():
            tableau[t_num1][-1].flip_card()
        return True
    return False
    
def check_win (stock, waste, foundation, tableau):
    '''check if everything is empty, except for foundation which has to be 4
    '''

    if stock.is_empty():
        if len(waste) == 0:
            if len(foundation) == 4:
                yes = 0
                for i in range(len(tableau)):
                    if len(tableau[i]) == 0:
                        yes +=1
                    else:
                        return False
                if yes == 7:
                    print("You've Won!")
                    return True
    return False    

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above

def main():   
    #####
    tableau, stock, foundation, waste = initialize()

    print(MENU)
    display(tableau,stock,foundation,waste)
    while True:
        try:
            while True:
                optionz = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
                parsed =parse_option(optionz)

                if parsed == None:
                    display(tableau,stock,foundation,waste)
                    continue
                if parsed[0] == "TT":
                    question=tableau_to_tableau(tableau, parsed[1]-1, parsed[2]-1)
                    if not question:
                        print("\nInvalid move!\n")
                    check_win(stock,waste,foundation,tableau)
                    if display(tableau,stock,foundation,waste):
                        exit()
                elif parsed [0] == "TF":
                    question = (tableau_to_foundation(tableau,foundation,parsed[1]-1,parsed[2]-1))
                    if not question:
                        print("\nInvalid move!\n")

                    display(tableau,stock,foundation,waste)
                    if check_win(stock,waste,foundation,tableau):
                        exit()
                elif parsed [0] == "WT":
                    question = (waste_to_tableau(waste,tableau,parsed[1]-1))
                    if not question:
                        print("\nInvalid move!\n")

                    display(tableau,stock,foundation,waste)
                    if check_win(stock,waste,foundation,tableau):
                        exit()
                elif parsed [0] == "WF":
                    (waste_to_foundation(waste,foundation,parsed[1]-1))
                    display(tableau,stock,foundation,waste)
                    if check_win(stock,waste,foundation,tableau):
                        exit()
                elif parsed [0] == "SW":
                    (stock_to_waste(stock,waste))
                    display(tableau,stock,foundation,waste)
                    if check_win(stock,waste,foundation,tableau):
                        exit()
                elif parsed [0] == "R":
                    tableau, stock, foundation, waste = initialize()
                    display(tableau,stock,foundation,waste)
                elif parsed [0] == "H":
                    print(MENU)
                elif parsed [0] == "Q":
                    exit()
                else:
                    pass
        except EOFError:
            break
    ####
if __name__ == '__main__':
     main()
