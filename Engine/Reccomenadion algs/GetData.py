import pandas as pd
from sqlalchemy import create_engine

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
    books.index = books['Book_ID']
    books.drop(['Book_ID'], axis = 1, inplace=True)

    books_des = pd.read_sql("Select Book_ID, Description as Des from book_app.base_book as book;", mydb)
    books_des.index = books_des['Book_ID']
    books_des.drop(['Book_ID'], axis = 1, inplace=True)

    books_genres = pd.read_sql("Select Book_ID_id AS Book_ID, Genre_ID_id AS Genre_ID from book_app.base_bookgenres as bookgenres Group By Book_ID_id, Genre_ID_id;", mydb)
    books_genres["Genre_ID"]= books_genres["Genre_ID"].astype("Sparse[int16]")
    books_genres.index = books_genres['Book_ID']
    books_genres.drop(['Book_ID'], axis = 1, inplace=True)
    books_genres = books_genres.groupby('Book_ID').agg(lambda col: col.tolist())

    return books, books_des, books_genres


def GetDataUsers():

    mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

    users = pd.read_sql("Select Reader_ID, Age, Sex from book_app.base_bookreaders", mydb)
    users.index = users['Reader_ID']
    users.drop(['Reader_ID'], axis = 1, inplace=True)

    users_history = pd.read_sql("SELECT br.Reader_ID, Date_Taken, Returned, Book_ID_id as Book_ID from book_app.base_history AS bh RIGHT JOIN book_app.base_bookreaders AS br ON br.Reader_ID = bh.Reader_ID_id WHERE Date_Taken >= DATE_SUB(NOW(),INTERVAL 6 MONTH)  OR Date_Taken IS NULL Group by Reader_ID, Book_ID Order BY Date_Taken, Reader_ID ", mydb)
    users_history['Date_Taken'] = users_history['Date_Taken'].dt.normalize()
    users_history.index = users_history['Reader_ID']
    users_history.drop(['Reader_ID'], axis = 1, inplace=True)


    users_wanted_books = pd.read_sql("Select Book_ID_id as Book_ID, Reader_ID_id as Reader_ID From book_app.base_userwantedbooks", mydb)
    

    users_genre_type = pd.read_sql("Select Genre_ID_id as Genre_ID, Reader_ID_id as Reader_ID From book_app.base_usergenre",mydb)    
    users_genre_type.index = users_genre_type['Reader_ID']
    users_genre_type.drop(['Reader_ID'], axis = 1, inplace=True)
    users_genre_type = users_genre_type.groupby('Reader_ID').agg(lambda col: col.tolist())

    return users, users_history, users_wanted_books, users_genre_type

def SendReccommendation():
    pass