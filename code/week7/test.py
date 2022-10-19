fp = open("data.csv", "r")

first_line = fp.readline()

output = []
for i in fp:
    i = i.strip().split(",")
    
    cara, rar, ele,wea,reg = i

    new_list = [cara, ele, wea,rar,reg]
    new_list = tuple(new_list)
    output.append(new_list)
print(output)