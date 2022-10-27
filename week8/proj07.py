# https://www.cse.msu.edu/~cse231/Online/Projects/Project07/Project07.pdf



GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s):
    ''' Docstring'''
    fp = open(f"{s}", "r", encoding="windows-1252")
    return fp

def read_users(fp):
    ''' split the user stats with | and reorder the 
    '''
    returns = [[]]

    for i in fp:
        a = i.strip().split("|")
        a[1] = int(a[1])
        a = tuple(a)
        returns.append(a[1:4])

    return returns

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
        
             

 
def read_movies(fp):
    ''' Docstring'''
    output = [[]]
    for i in fp:
        a =i.strip().split("|")

        matches = []                
        for j in range(len(a)-5): # the 0/1 starts at 5
            if((a[j+5])) == "1": # ^^
                matches.append(GENRES[j])
        a = a[1:3]
        a.append(matches)
        output.append(tuple(a))
    return(output)



def year_movies(year,L_movies):
    year = int(year)

    matches = []
    for i, strs in enumerate(L_movies[1:], 1):
        a = strs[1].split("-")
        
        if a[-1] == "":
            continue

        if int(a[-1]) == year:
            matches.append(i)
    return matches
    

def genre_movies(genre,L_movies):

    matches = []
    genre = genre.lower()

    for i, strs in enumerate(L_movies[1:], 1):
        strs = strs[-1]

        tmp_list = []
        for j in strs:
            tmp_list.append(j.lower())

        if genre in tmp_list:
            matches.append(i)


    return matches

def gen_users (gender, L_users, L_reviews):
    ''' Docstring'''
    returns = []
    for i, strs in enumerate(L_users[1:], 1):
        if gender in strs:
            returns.append(L_reviews[i])
    return(returns)


def occ_users (occupation, L_users, L_reviews):
    ''' Docstring'''
    returns = []
    for i, strs in enumerate(L_users[1:], 1):
        if occupation in strs:
            returns.append(L_reviews[i])
    return(returns)

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    # i is movie id, j is movie score
    find_list = [[0,0] for _ in range(N_movies+1)]
    for k in L_in:
        score_total = 0
        seen = 0
        for i in range(len(L_reviews)):
            len_list = len(L_reviews[i])

            for j in range(len_list):

                if k in L_reviews[i][j]:
                    if L_reviews[i][j][0] != k:
                        continue
                    else:
                        score_total += L_reviews[i][j][1]
                        seen +=1
        
        find_list[k]= [score_total, seen]
    
    # print(find_list)

    avg_list = find_list[:]
    for i in range(len(find_list)):
        try:
            avg_list[i] = float(f"{avg_list[i][0]/avg_list[i][1]:.2f}")
        except ZeroDivisionError:
            avg_list[i] = 0
            continue
    max_list = max(avg_list)
    # print(max_list)
    movies_find = []
    for i in range(len(avg_list)):
        if max_list == avg_list[i]:
            movies_find.append(i)
    
    return movies_find, max_list




def highest_rated_by_reviewer(L_in,N_movies):
    #(movieid, rating)
    #[score_tota, seen]
    ''' Docstring'''
    list_of_moives = [[0,0] for _ in range(N_movies+1)]

    for i in range(len(L_in)):
        

        for j in range(len(L_in[i])):

            element = L_in[i][j][0]
            list_of_moives[element][0] += 1
            # print(list_of_moives)
            movie_score = L_in[i][j][1]
            list_of_moives[element][1] += movie_score
            

    avg_list = list_of_moives[:] 
    for i in range(len(avg_list)):
        try:
            avg_list[i] = float(f"{avg_list[i][1]/avg_list[i][0]:.2f}")
        except ZeroDivisionError:
            avg_list[i] = 0
            continue
    max_value = max(avg_list)
    find_index_of_max = []
    for i in range(len(avg_list)):
        if avg_list[i] == max_value:
            find_index_of_max.append(i)

    return find_index_of_max, max_value


    




def main():

    N = 10

    L_in = [[(1,1),(0,0),(5,1),(7,1)],
        [(1,2),(3,4),(5,2),(2,0),(7,2),(9,2)],
        [(2,3),(4,3),(6,3),(8,3),(7,3),(3,3)],
        [(2,4),(4,4),(6,4),(8,4)],
        [(2, 2), (10, 2)]]

    print(highest_rated_by_reviewer(L_in,N))
















    # users = input("Input users filename: ")
    # reviews = input("Input reviews filename: ")
    # movies = input("Input movies filename: ")


    # users = "users.txt"
    # reviews = "reviews_small.txt"
    # movies = "movies_small.txt"


    # movies_fp = open_file(movies)
    # L_movies = read_movies(movies_fp)

    # reviews_fp = open_file(reviews)
    # N = 0
    # for i in reviews_fp:
    #     i =i.split()
    #     if int(i[0]) > N:
    #         N = int(i[0])
    # reviews_fp = open_file(reviews)
    # L_reviews = read_reviews(N+1, reviews_fp)
    





    # print(MENU)
    # optionz = input()

    # if optionz == "1":
        # year = int(input("Input a year: "))
        # returned = year_movies(year,L_movies)
        # highest_rated_by_movie(returned, L_reviews, N)








if __name__ == "__main__":
    main()
                                           
