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
    ''' Docstring'''
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
        
    ''' Docstring'''
    pass   # remove this line

    ''' Docstring'''
    pass   # remove this line


          

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    pass   # remove this line
             
def highest_rated_by_reviewer(L_in,N_movies):
    ''' Docstring'''
    pass   # remove this line
 
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
    for i, strs  in enumerate(L_movies):
        if strs == []:
            continue
        a = strs[1].split("-")
        
        if a[-1] == "":
            continue

        if int(a[-1]) == year:
            matches.append(i)
    return matches
    

def genre_movies(genre,L_movies):

    matches = []
    genre = genre.lower()

    for i, strs in enumerate(L_movies):
        if strs == []:
            continue
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
    for i, strs in enumerate(L_users):
        if strs == []:
            continue
        if gender in strs:
            returns.append(L_reviews[i])
    return(returns)


def occ_users (occupation, L_users, L_reviews):
    ''' Docstring'''
    returns = []
    for i, strs in enumerate(L_users):
        if strs == []:
            continue
        if occupation in strs:
            returns.append(L_reviews[i])
    return(returns)






def main():





    # moves_fp = open_file("movies_small.txt")

    # L_movies = (read_movies(moves_fp))


#
    fp = open_file("reviews_small.txt")
    N = 0
    
    for i in fp:
        if int(i[0]) > N:
            N = int(i[0])
    
    fp = open_file("reviews_small.txt")
    L_reviews = read_reviews(N, fp)
#

    users_fp = open_file("users_small.txt")

    L_users = read_users(users_fp)

    occ_users("technician", L_users, L_reviews)
    










    # gen_users("F", L_users, L_reviews)
    

    # year = 1940
    # print(year_movies(year, L_movies))












    ###





    ###

    

    ###
    # print(read_users(open_file("users_small.txt")))

    



























if __name__ == "__main__":
    main()
                                           
