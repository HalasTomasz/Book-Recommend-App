import pandas as pd
from sqlalchemy import create_engine
import MySQLdb

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
    books_genres = books_genres.groupby('Book_ID', as_index=False).agg(lambda col: col.tolist())


    return books, books_des, books_genres


def GetDataUsers():

    mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

    users = pd.read_sql("Select Reader_ID, Age, Sex from book_app.base_bookreaders", mydb)
    users.index = users['Reader_ID']
    users.drop(['Reader_ID'], axis = 1, inplace=True)

    users_history = pd.read_sql("SELECT Reader_ID_id AS Reader_ID, Date_Taken, Returned, Book_ID_id as Book_ID  from book_app.base_history WHERE Date_Taken >= DATE_SUB(NOW(),INTERVAL 6 MONTH)  AND Reader_ID_id IN ( SELECT Reader_ID_id AS Reader_ID from book_app.base_history WHERE Date_Taken >= DATE_SUB(NOW(),INTERVAL 6 MONTH)   GROUP  BY Reader_ID HAVING COUNT(Book_ID_id) > 3 ) Order BY Date_Taken, Reader_ID  ", mydb)
    # users_history['Date_Taken'] = users_history['Date_Taken'].dt.normalize()
    # users_history.index = users_history['Reader_ID']
    # users_history.drop(['Reader_ID'], axis = 1, inplace=True)
 
    users_genre_type = pd.read_sql("Select Genre_ID_id as Genre_ID, Reader_ID_id as Reader_ID From book_app.base_usergenre",mydb)    
    users_genre_type.index = users_genre_type['Reader_ID']
    users_genre_type.drop(['Reader_ID'], axis = 1, inplace=True)
    users_genre_type = users_genre_type.groupby('Reader_ID').agg(lambda col: col.tolist())

    return users, users_history, users_genre_type

def DoSurvey():
    mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
    
    sql = "SELECT DISTINCT bk.name, bk.Book_ID as Book_ID FROM book_app.base_book  AS bk ORDER BY NumberReviews DESC LIMIT 50"
    df = pd.read_sql(sql,con=mydb)

    return [int(x)-1 for x in df['Book_ID']]
    
def SendReccommendation(reccomendtions):
 
    db=MySQLdb.connect("localhost","root","Tajne123","book_app")
    c=db.cursor()
 
    c.executemany(
      """INSERT INTO base_algorithmrecomendations (Alogritm_ID, Book_ID_id, Reader_ID_id) VALUES (%s, %s, %s)""",
     reccomendtions)

    db.commit()

    db.close()
    