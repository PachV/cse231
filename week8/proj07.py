
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
    pass   # remove this line

def read_reviews(N,fp):
    ''' Docstring'''
    pass   # remove this line

def read_users(fp):
    ''' Docstring'''
    pass   # remove this line

def read_movies(fp):
    ''' Docstring'''
    pass   # remove this line
        
def year_movies(year,L_movies):
    ''' Docstring'''
    pass   # remove this line

def genre_movies(genre,L_movies):
    ''' Docstring'''
    pass   # remove this line

def gen_users (gender, L_users, L_reviews):
    ''' Docstring'''
    pass   # remove this line
          
def occ_users (occupation, L_users, L_reviews):
    ''' Docstring'''
    pass   # remove this line

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    pass   # remove this line
             
def highest_rated_by_reviewer(L_in,N_movies):
    ''' Docstring'''
    pass   # remove this line
 
def main():
    pass   # remove this line

if __name__ == "__main__":
    main()
                                           
