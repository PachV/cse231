def add_to_dict(dict,key,value):
    if key in dict:
        print("Error. Key already exists.")
        return dict
    dict[key] = value
    return dict

def remove_from_dict(dict, key):
    try:
        del dict[key] 
    except KeyError:
        print("No such key exists in the dictionary.")
        return dict
    return dict


def find_key(dict, key):
    try:
        value =dict[key] 
        print(f"Value:  {value}")
    except KeyError:
        print("Key not found.")
        return dict


def main():
    more = True
    dictt = {}
    dictlst = []
    while more:      
        print("Menu: ")
        choice = input("add(a), remove(r), find(f): \n")
        if choice.lower() == "a":
            key = input("Key: \n")
            value = input("Value: \n")
            dictt = add_to_dict(dictt, key,value)
        elif choice.lower() == "r":
            key = input("key to remove: \n")
            dictt = remove_from_dict(dictt,key)
        elif choice.lower() == "f":
            key = input("Key to locate: \n")
            find_key(dictt,key)
        else:
            print("Invalid choice.")
            
        do_more = input("More (y/n)? \n")
        if do_more.lower() != 'y':
            more = False



    if dictt:
      for key, value in dictt.items():
          temp = (key,value)
          dictlst.append(temp)
      print(sorted(dictlst))
main()