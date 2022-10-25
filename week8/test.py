from decimal import DivisionByZero


def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    # i is movie id, j is movie score
    find_list = [[0,0] for _ in range(N_movies+1)]
    L_in = [1,2,3,6,7]
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
    #     # average can be done by a[1][0]/a[1][1]
        try:
            avg_list[i] = float(f"{avg_list[i][0]/avg_list[i][1]:.2f}")
        except ZeroDivisionError:
            avg_list[i] = 0
            continue
    print(avg_list) 



N = 10
L_reviews = [[], [(2, 3), (3, 3), (6, 1), (9, 5), (10, 2)], 
            [(3, 1), (4, 4), (5, 3), (6, 5), (7, 3), (8, 5)], 
            [(1, 2), (4, 3), (7, 3)], [(10, 5)], [],
            [(2, 2), (5, 2), (8, 3)], [], [],
            [(2, 2), (10, 4)], []]
L1 = [1,2,3,6,7]   # indexs  
[[0, 0], [2, 1], [7, 3], [4, 2], [0, 0], [0, 0], [6, 2], [6, 2], [0, 0], [0, 0], [0, 0]]
highest_rated_by_movie(L1,L_reviews, N)


