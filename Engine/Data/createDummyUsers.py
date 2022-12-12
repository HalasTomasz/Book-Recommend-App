import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from scipy.spatial.distance import pdist
import scipy.cluster.hierarchy as sch
import collections
from datetime import date
import MySQLdb
import seaborn as sns
import matplotlib.pyplot as plt

user = 'root'
passw = 'Tajne123'
host =  'localhost'  # either localhost or ip e.g. '172.17.0.2' or hostname address 
port = 3306 
database = 'book_app'


def GetDataBooks():

    mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
    
    books = pd.read_sql("Select Book_ID, Name, Availability, Rating, NumberReviews, Author_Name   from book_app.base_book as book Inner Join book_app.base_bookauthor as author on author.Author_ID =  book.Author_ID;  ", mydb)
    books["Availability"]= books["Availability"].astype("Sparse[int8]")
    books["NumberReviews"]= books["NumberReviews"].astype("Sparse[int]")
    
    books_des = pd.read_sql("Select Book_ID, Description as Des from book_app.base_book as book;", mydb)

    books_genres = pd.read_sql("Select Book_ID_id AS Book_ID, Genre_ID_id AS Genre_ID from book_app.base_bookgenres as bookgenres Group By Book_ID_id, Genre_ID_id;", mydb)
    books_genres["Genre_ID"]= books_genres["Genre_ID"].astype("Sparse[int16]")
    books_genres = books_genres.groupby('Book_ID').agg(lambda col: col.tolist())

    return books, books_des, books_genres

    
def GetDataUsers():

    mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

    users = pd.read_sql("Select Reader_ID, Age, Sex from book_app.base_bookreaders", mydb)
    users.index = users['Reader_ID']
    users.drop(['Reader_ID'], axis = 1, inplace=True)

    users_history = pd.read_sql("SELECT br.Reader_ID, Date_Taken, Returned, Book_ID_id as Book_ID from book_app.base_history AS bh RIGHT JOIN book_app.base_bookreaders AS br ON br.Reader_ID = bh.Reader_ID_id WHERE Date_Taken >= DATE_SUB(NOW(),INTERVAL 6 MONTH)  OR Date_Taken IS NULL Group by Reader_ID, Book_ID Order BY Date_Taken, Reader_ID ", mydb)
    # users_history['Date_Taken'] = users_history['Date_Taken'].dt.normalize()
    # users_history.index = users_history['Reader_ID']
    # users_history.drop(['Reader_ID'], axis = 1, inplace=True)
 

    users_wanted_books = pd.read_sql("Select Book_ID_id as Book_ID, Reader_ID_id as Reader_ID From book_app.base_userwantedbooks", mydb)
    

    users_genre_type = pd.read_sql("Select Genre_ID_id as Genre_ID, Reader_ID_id as Reader_ID From book_app.base_usergenre",mydb)    
    users_genre_type.index = users_genre_type['Reader_ID']
    users_genre_type.drop(['Reader_ID'], axis = 1, inplace=True)
    users_genre_type = users_genre_type.groupby('Reader_ID').agg(lambda col: col.tolist())

    return users, users_history, users_wanted_books, users_genre_type

def setUserGender(gender_val):

     if gender_val < 0.45:
        return 'Man'
     elif gender_val > 0.55: 
        return 'Woman'
     else:
        return 'No'


def setUser(gender_val):

    if gender_val < 0.45:
        return 'Man'
    elif gender_val > 0.55: 
        return 'Woman'
    else:
        return 'No'


def createGenreBooks(books_genre_df):

    groups = {}
    for lst in list(books_genre_df['Genre_ID']):
        for x in lst:
            if x in groups:
                for y in lst:
                    if x!=y:
                        if y in groups[x]:
                              groups[x][y] = groups[x][y] + 1
                        else:
                              groups[x][y] = 1
                    
            else:
                groups[x] = {}
    
    od = collections.OrderedDict(sorted(groups.items())) # ma 962 elementów ale zawiera używane i isntiejące gatunki!
    x = 0 
    array_of_array = []
    keys_arr = [] 
    for key, val in od.items():
        tmp = []
        keys_arr.append(key)
        for x in range(1,len(groups)+1):
            if x in val:
                tmp.append(val[x])
            else:
                tmp.append(0)
        array_of_array.append(tmp)
    array_of_array = np.array(array_of_array)   
    df= pd.DataFrame(array_of_array, index=keys_arr, columns=keys_arr)
    print(df)
    df_corr = df.corr(method='spearman')
    df_corr = df_corr.dropna(axis='columns',how='all')
    df_corr = df_corr.dropna(axis='rows',how='all')
    print(df_corr)
    plt.scatter(df.iloc[[0]], df.iloc[[2]])

    plt.show()
    converter = {}
    indexs = 0 
    for el in list(df_corr.index):
        converter[indexs] =  el
        indexs = indexs + 1

    pdist_data = pdist(df_corr)
    linkage_arr = sch.linkage(pdist_data, method='ward')
    idx_to_cluster_array = sch.fcluster(linkage_arr,  t=6, criterion='maxclust')
    print(idx_to_cluster_array)
    idx = np.argsort(idx_to_cluster_array)
    print(idx)

    claster_dict = {}

    for claster, element in zip(idx_to_cluster_array, idx):
        if claster in claster_dict.keys():

            claster_dict[claster].append(converter[element])
        else:
            claster_dict[claster] = [converter[element]]
  
    
    for key, val in claster_dict.items():
        print("Klaster nr:" ,key)
        print("(", end='')
        for el in val:
            print(el," , ", end='')
        print(")", end='\n')
    
 
    print(len(converter))

def main_func():

    books, booksDes, booksGenre = GetDataBooks() # Get DF hereZ
    users, usersHistory, userWantednBooks, usersGenre = GetDataUsers()
    createGenreBooks(booksGenre)



def createSimplyDummyUser():

    books, booksDes, booksGenre = GetDataBooks()
    numberOFUser = 50
    id_of_user_in_db = 52 # REMBER TO SET THIS
    user_arr = []
    user_hist= []
    user_review = []
    user_review_db = [] 
    user_genres = []
    np.random.seed(100) # Setting seed
    for i in range(id_of_user_in_db, numberOFUser+ id_of_user_in_db):
        user_genre_data =  np.random.randint(1, 70, size=np.random.randint(1,5))
        user_history_data = np.random.randint(1, 30, size=np.random.randint(1,5))
        for idOfBooks in user_history_data:
            user_review.append(np.random.normal(float(books.iloc[idOfBooks-1]['Rating']),1))
        name = 'radnom_user ' + str(i)
        user_arr.append((name, None, '0', 'NO'))
        for id,review in zip(user_history_data,user_review) :
            user_hist.append((date.today(),False,id,i))
            user_review_db.append((date.today(),review,id,i))
        
        for genres in user_genre_data:
             user_genres.append((genres,i))
    #user_review = [tuple(x) for x in user_review]
    print(user_arr)
    print()
    print(user_hist)
    print()
    print(user_review_db)
    print()
    print(user_genres)
    db=MySQLdb.connect("localhost","root","Tajne123","book_app")
    c=db.cursor()
 
    c.executemany(
      """INSERT INTO base_usergenre (Genre_ID_id, Reader_ID_id) VALUES (%s, %s)""",
     user_genres)

    c.executemany(
      """ INSERT INTO base_history (Date_Taken, Returned, Book_ID_id, Reader_ID_id) VALUES (%s, %s,%s, %s)""",
     user_hist)

    c.executemany(
      """INSERT INTO base_review (Date, Review, Book_ID_id, Reader_ID_id) VALUES (%s, %s,%s,%s)""",
     user_review_db)

    # c.executemany(
    #   """INSERT INTO base_bookreaders (Name, FireBaseAuth, Age, Sex) VALUES (%s, %s,%s,%s)""",
    #  user_arr)


    

    # mycursor = mydb.cursor()
 
    # sql = "INSERT INTO base_bookreaders (Name, FireBaseAuth, Age, Sex) VALUES (%s, %s,%s,%s)"

    # mycursor.executemany(sql, [(r) for r in user_arr])
   # mycursor.execute(sql, ','.join(user_arr))

#     sql = "INSERT INTO base_review (Date, Review, Book_ID_id, Reader_ID_id) VALUES (%s, %s,%s,%s)"
#     #
#     # mycursor.execute(sql, ','.join(user_review_db))
#     mycursor.executemany(sql, [(r) for r in user_review_db])
#     sql = "INSERT INTO base_usergenre (Genre_ID_id, Reader_ID_id) VALUES (%s, %s)"
#    #
#    #  mycursor.execute(sql, ','.join(user_genres))
#     mycursor.executemany(sql, [(r) for r in user_genres])

#     sql = "INSERT INTO base_history (Date_Taken, Returned, Book_ID_id, Reader_ID_id) VALUES (%s, %s,%s,%s)"
#     #mycursor.execute(sql, ','.join(user_hist))

#     mycursor.executemany(sql, [(r) for r in user_hist])


main_func()