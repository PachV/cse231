def read_reviews(N,fp):
    ''' Docstring'''
    output = [[] for _ in range(N+1)]
    for i in fp:
        ind_list = i.split()
        a = [int(x) for x in ind_list]
        output[a[0]].append(tuple(a[1:3]))
    
    for i in range(len(output)):
        output[i].sort()

    return(output)
        

def open_file(s):
    ''' Docstring'''
    fp = open(f"{s}", "r", encoding="windows-1252")
    return fp

reviews = "reviews_small.txt"
reviews_fp = open_file(reviews)
N = 0
for i in reviews_fp:
    i =i.split()
    if int(i[0]) > N:
        N = int(i[0])
reviews_fp = open_file(reviews)
L_reviews = read_reviews(N+1, reviews_fp)
print(L_reviews)
