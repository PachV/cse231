#https://www.cse.msu.edu/~cse231/Online/Projects/Project08/Project08.pdf

MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    '''Docstring'''
    file_name = input(f"Input a {s} file: ")
    while True:
        try:
            fp = open(f"{file_name}", "r")
            return fp
        except FileNotFoundError:
            print("Not found, try again")
            file_name = input(f"Input a {s} file: ")

def read_names(fp):
    '''Docstring'''
    names = []
    for i in fp:
        names.append(i.strip())
    return names



def read_friends(fp,names_lst):
    '''Docstring'''
    output = []
    for i in fp:
        i =list(i.replace(",", "").replace(" ", "").strip())
        tmp_list = []
        for j in i:
            j = int(j)
            tmp_list.append(names_lst[j])
        output.append(tmp_list)
    return output



def create_friends_dict(names_lst,friends_lst):
    '''Docstring'''
    return {names_lst: friends_lst for names_lst, friends_lst in zip(names_lst, friends_lst) }

            
def find_common_friends(name1, name2, friends_dict):
    '''Docstring'''
    name1_list = friends_dict[name1]
    name2_list = friends_dict[name2]
    name1_set = set(name1_list)
    name2_set = set(name2_list)
    common = name1_set.intersection(name2_set) # same as (name1 & name2) sets
    return common

def find_max_friends(names_lst, friends_lst):
    '''Docstring'''
    max_val = 0
    new_dict = dict()
    for i in range(len(names_lst)):
        new_key = len(friends_lst[i])

        if new_key in new_dict:
            new_dict[new_key].append(names_lst[i])
            
        else:
            new_dict[new_key] = [names_lst[i]]

    key_values=list(new_dict.keys())
    for i in key_values:
        if i > max_val:
            max_val = i

    max_friends = new_dict[max_val]
    max_friends.sort()

    return max_friends, max_val 
         
def find_max_common_friends(friends_dict):
    '''Docstring'''
    possible_pairs = []
    results_dict = dict()
    max = 0

    for i in friends_dict:
        for j in friends_dict:
            if i != j:
                if (i,j) and (j,i) in possible_pairs:
                    continue
                else:
                    possible_pairs.append((i,j))
            else:
                continue
    
    for i in range(len(possible_pairs)):
        # print(possible_pairs[i][0], possible_pairs[i][1])
        name1 = possible_pairs[i][0]
        name2 = possible_pairs[i][1]
        names1_list = friends_dict[name1]
        names2_list = friends_dict[name2]

        names1_set = set(names1_list)
        names2_set = set(names2_list)
        
        common = names1_set.intersection(names2_set)

        if name1 in common:
            common.remove(name1) 
        if name2 in common:
            common.remove(name2)
        new_key = len(common)
        

        if new_key in results_dict:
            results_dict[new_key].append((name1,name2))
        else:
            results_dict[new_key] = [(name1,name2)]

    keys = list(results_dict.keys())
    for i in keys:
        if i > max:
            max = i
    common_friends = results_dict[max]
    return common_friends,max

def find_second_friends(friends_dict):
    '''Docstring'''
    new_dict = dict()

    for i in friends_dict:
        f_of_f = []
        friends = friends_dict[i]
        for j in friends:
            f_of_f += friends_dict[j]
        f_of_f = set(f_of_f)
        # print(f_of_f)
        for j in friends:
            if j in f_of_f:
                f_of_f.remove(j)
        f_of_f.remove(i)
        new_dict[i] = f_of_f
    return new_dict 


def find_max_second_friends(seconds_dict):
    '''Docstring'''
    new_dict = dict()
    max_val = 0
    for i in seconds_dict:
        friends = seconds_dict[i]
        new_key = int(len(friends))

        if new_key in new_dict:
            new_dict[new_key].append([i])
        else:
            new_dict[new_key] = [i]

    key_values=list(new_dict.keys())
    for i in key_values:
        if i > max_val:
            max_val = i
    max_friends = new_dict[max_val]
    max_friends.sort()
    return max_friends, max_val 














def main():

    fp = open("Names_small.txt", "r")
    names_lst = read_names(fp)
    fp = open("Friends_small.csv", "r")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst, friends_lst)
    seconds_dict = find_second_friends(friends_dict)
    print(find_max_second_friends(seconds_dict))

    # print("\nFriend Network\n")
    # fp = open_file("names")
    # names_lst = read_names(fp)
    # fp = open_file("friends")
    # friends_lst = read_friends(fp,names_lst)
    # friends_dict = create_friends_dict(names_lst,friends_lst)

    # print("\nFriend Network:")
    # for name,friends in friends_dict.items():
    #     print(name,":")
    #     print("   {}".format(friends))

    # print(MENU)
    # choice = input("\nChoose an option: ")
    # while choice not in "12345":
    #     print("Error in choice. Try again.")
    #     choice = input("Choose an option: ")
        
    # while choice != '5':

    #     if choice == "1":
    #         max_friends, max_val = find_max_friends(names_lst, friends_lst)
    #         print("\nThe maximum number of friends:", max_val)
    #         print("People with most friends:")
    #         for name in max_friends:
    #             print(name)
                
    #     elif choice == "2":
    #         max_names, max_val = find_max_common_friends(friends_dict)
    #         print("\nThe maximum number of commmon friends:", max_val)
    #         print("Pairs of non-friends with the most friends in common:")
    #         for name in max_names:
    #             print(name)
                
    #     elif choice == "3":
    #         seconds_dict = find_second_friends(friends_dict)
    #         max_seconds, max_val = find_max_second_friends(seconds_dict)
    #         print("\nThe maximum number of second-order friends:", max_val)
    #         print("People with the most second_order friends:")
    #         for name in max_seconds:
    #             print(name)
                
    #     elif choice == "4":
    #         pass  # YOUR CODE GOES HERE

    #     else: 
    #         print("Shouldn't get here.")
            
    #     choice = input("\nChoose an option: ")
    #     while choice not in "12345":
    #         print("Error in choice. Try again.")
    #         choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
