######################## 
# Proj07
# User inputs the 3 needed files names, which is users,reviews,movies
# user will select the option from 1-5
# program will match the option from 1-5 
# and will ask the user for the required items in that opiton
# then prints out the max avg rating for that input and the movies\
#  corresponding do it 
# keeps asking for options until str 5 is entered, then exit the program 
########################

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
    ''' returns the file pointer with the parameter as the file'''
    fp = open(f"{s}", "r", encoding="windows-1252")
    return fp

def read_users(fp):
    ''' read each line in the file
        split the user stats with | and reorder the the list
        convert the 2nd element to int because its a num
        and only return the age, gender and occupation
    '''
    returns = [[]]

    for i in fp:
        a = i.strip().split("|")
        a[1] = int(a[1]) 
        a = tuple(a)
        returns.append(a[1:4]) # we only need [1:4]

    return returns

def read_reviews(N,fp):
    ''' 
        N is the length of the list, and fp is file pointer
        reorder the list to their coresponding movie id and score
        (movieid, score)
    
    '''
    output = [[] for _ in range(N+1)] # make each element seperate addresses
    for i in fp:
        ind_list = i.split()
        a = [int(x) for x in ind_list] # convert all to int
        output[a[0]].append(tuple(a[1:3])) # the index will be the value
    
    for i in range(len(output)):
        output[i].sort()

    return(output)
 
def read_movies(fp):
    ''' returns a list of the movies and the year publishsed,
        and the kind of genres it has
    ''' 
    output = [[]]
    for i in fp:
        a =i.strip().split("|")

        matches = []                
        for j in range(len(a)-5): # the 0/1 starts at 5th index
            if((a[j+5])) == "1": # ^^
                matches.append(GENRES[j]) # if 1 then its true
        a = a[1:3]
        a.append(matches)
        output.append(tuple(a))
    return(output)

def year_movies(year,L_movies):
    '''
        match the year of the movie in the list,
        and return the movie's index in L_movies
    '''
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
    '''
        match the genre with L_movies and return the
        index of it
    '''
    matches = []
    genre = genre.lower()

    for i, strs in enumerate(L_movies[1:], 1):
        strs = strs[-1] # only need last element content
        tmp_list = []
        for j in strs:
            tmp_list.append(j.lower())

        if genre in tmp_list:
            matches.append(i)

    return matches

def gen_users(gender, L_users, L_reviews):
    ''' match the gender in L_users and 
        return a new list with movieid and
        scores stuff with the respected gender
    '''
    returns = []
    for i, strs in enumerate(L_users[1:], 1):
        if gender in strs:
            returns.append(L_reviews[i])
    return returns

def occ_users(occupation, L_users, L_reviews):
    ''' 
        match the occupation in L_users and
        return a new list with the movieid and 
        score with the respected occupation
    '''
    returns = []
    for i, strs in enumerate(L_users[1:], 1):
        if occupation in strs:
            returns.append(L_reviews[i])
    return returns

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    '''
        make a N length list of 0,0 with N_movies,
        L_in are the numbers we want to keep
        from L_review(movieid, score), make the new list
        with the according moveid num to the new list element
        add the total score in the 0th index, and seen in 1st index
        find the average by doing total_score/seen
        and find the max average
        with max average,  find the each index that matches with max average/
         for the movieid.
        and return the movieid/index with that max average, and max average

    '''
    find_list = [[0,0] for _ in range(N_movies+1)]
    for k in L_in:
        score_total = 0
        seen = 0
        for i in range(len(L_reviews)):
            len_list = len(L_reviews[i])

            for j in range(len_list):

                if k in L_reviews[i][j]: # now reading elemnts in list of list
                    if L_reviews[i][j][0] != k: # check if the movie is k value
                        continue
                    else:
                        score_total += L_reviews[i][j][1]
                        seen +=1

        find_list[k]= [score_total, seen]
    
    avg_list = find_list[:] # copying just in case
    for i in range(len(find_list)):
        try:
            avg_list[i] = float(f"{avg_list[i][0]/avg_list[i][1]:.2f}")
        except ZeroDivisionError:
            avg_list[i] = 0
            continue
    max_list = max(avg_list)
    movies_find = []
    for i in range(len(avg_list)):
        if max_list == avg_list[i]: # find the index that is equal to max value
            movies_find.append(i)
    
    return movies_find, max_list

def highest_rated_by_reviewer(L_in,N_movies):
    '''         
        make a N length list of 0,0 with N_movies,
        L_in is a list from specific group of users

        the movieid corresponds with the indext of new list
        add the moveid seen and the score in the index of the moveid
        then find the average by doing division
        and return the highest max value and the index/movieid of it
    '''
    list_of_moives = [[0,0] for _ in range(N_movies+1)]

    for i in range(len(L_in)):
        
        for j in range(len(L_in[i])):

            element = L_in[i][j][0]
            list_of_moives[element][0] += 1
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

    users = input("\nInput users filename: ")
    reviews = input("\nInput reviews filename: ")
    movies = input("\nInput movies filename: ")
    
    user_fp = open_file(users)
    L_users = read_users(user_fp)
    
    movies_fp = open_file(movies)
    L_movies = read_movies(movies_fp)

    reviews_fp = open_file(reviews)
    print(MENU) 

    # finds the largest value of N so we can
    # call functions with the correct amount of 
    # elements
    N = 0
    for i in reviews_fp:
        i =i.split()
        i_int = int(i[1])
        if i_int > N:
            N = i_int

    reviews_fp = open_file(reviews)
    L_reviews = read_reviews(N, reviews_fp)

    while True:
        optionz = input("\nSelect an option (1-5): ")

        if optionz == "1":
            while True:
                
                year = int(input("\nInput a year: "))
                returned = year_movies(year,L_movies)
                # a is the indexes of the filtered lists
                a, rat = highest_rated_by_movie(returned, L_reviews, N)
                
                tmp_print_list = []
                try:
                    for i in a:
                            tmp_str = (L_movies[i][0])
                            tmp_print_list.append(tmp_str)
                except IndexError:
                    print("\nError in year.")
                    continue
                print(f"\nAvg max rating for the year is: {rat}")
                for i in tmp_print_list:
                    print(i)
                break

        elif optionz == "2":
            print(f"\nValid Genres are:  {GENRES}")
            while True:
                genre = input("Input a genre: ").lower().capitalize()
                L_in =(genre_movies(genre, L_movies))
                # a is the indexes of the filtered lists
                a, rat = highest_rated_by_movie(L_in, L_reviews, N)

                tmp_print_list = []
                try:
                    for i in a:
                        tmp_print_list.append(L_movies[i][0])
                except IndexError:
                    print("\nError in genre.")
                    continue

                print(f"\nAvg max rating for the Genre is: {rat}")
                for i in tmp_print_list:
                    print(i)
                break
            continue

        elif optionz == "3":
            while True:
                gen = input("\nInput a gender (M,F): ").upper()
                
                if gen == "M" or gen == "F":
                    L_in = gen_users(gen, L_users, L_reviews)
                    a ,rat = highest_rated_by_reviewer(L_in, N)

                    print(f"\nAvg max rating for the Gender is: {rat}")
                    for i in a:
                        print(L_movies[i][0])
                    break
                else:
                    print("\nError in gender.")
                    continue

        elif optionz == "4":
            print(f"\nValid Occupatipns are:  {OCCUPATIONS}")    
            while True:
                occu = input("Input an occupation: ").lower()

                if occu in OCCUPATIONS:
                    L_in =occ_users(occu,L_users,L_reviews) 
                    a, rat = highest_rated_by_reviewer(L_in,N)
                    
                    print(f"\nAvg max rating for the occupation is: {rat}")
                    for i in a:
                        print(L_movies[i][0])
                    break
                else:
                    print("\nError in occupation.")
                    continue

        elif optionz == "5":
            exit()
        else:
            print("\nError: not a valid option.")
            continue

if __name__ == "__main__":
    main()
                                           
