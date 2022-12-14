from base64 import encode
import string
import pandas as pd
import numpy as np
from ast import literal_eval
from MySQLdb.constants import FIELD_TYPE
from sqlalchemy import create_engine
import re

my_conv = { FIELD_TYPE.LONG: int,
            FIELD_TYPE.DECIMAL: float,
            FIELD_TYPE.VARCHAR: string,
        }

user = 'root'
passw = 'Tajne123'
host =  'localhost'  # either localhost or ip e.g. '172.17.0.2' or hostname address 
port = 3306 
database = 'book_app'

def getAuthorsDict(df, mydb):

    series_books = df.drop_duplicates()
    df_author = pd.DataFrame(series_books)
    authors_dict = pd.Series(list(range(1, len(series_books) +1)), index=series_books.astype(str) ).to_dict()
    df_author['Author_Name'] = df_author['Author_Name'].map(lambda x: x.replace(' (Goodreads Author)','') if ' (Goodreads Author)' in x else x)
    df_author.to_sql(name='base_bookauthor', con=mydb, if_exists = 'append', index=True, index_label='Author_ID')

def getGenreDict(df, mydb):

    series_genre= df.drop_duplicates()

    genre_dict = pd.Series(list(range(1, len(series_genre)+1)), index=series_genre.astype(str) ).to_dict() 

    df_genre = pd.DataFrame(series_genre)
    df_genre.reset_index(drop=True,inplace=True)
    
    df_genre.to_sql(name='base_genre', con=mydb, if_exists = 'append', index=True, index_label='Genre_ID')
    

def getUserGenre(mydb):
    genre_array = []
    with open('dane.txt') as file:

        for line in file:
            genre_array.append(line.split(",")[0].strip())

    df = pd.DataFrame(genre_array, columns=["Genre_Name"])

    df.to_sql(name='base_genreshort', con=mydb, if_exists = 'append', index=True, index_label='Genre_ID')

def readDataExcel(path_file_name='./books_1.Best_Books_Ever.csv'):

    df_books = pd.read_csv(path_file_name, usecols=['Name', 'Author_Name', 'language', 'Rating', 'Description', 'Genre_Name', 'NumberReviews', 'ImgSource'])
    #con = MySQLdb.connect(conv= my_conv, host="localhost",user="root", passwd="Tajne123",db="book_app") 
    
    mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
    
    #author_dict = getAuthorsDict(df_books['Author_Name'], mydb)
    df_books = df_books[df_books['language'] == 'English']
    df_books['Genre_Name'] = df_books['Genre_Name'].apply(literal_eval) #convert to list type
    df_books= df_books.explode('Genre_Name')
    All_genres = pd.read_sql("Select * from book_app.base_genre", mydb)
    genre_dict = {}
    for index, name in zip(All_genres['Genre_ID'],All_genres['Genre_Name']):
        genre_dict[name] = index
    
    All_Authors = pd.read_sql("Select * from book_app.base_bookauthor", mydb)
    author_dict = {}
    for index, name in zip(All_Authors['Author_ID'],All_Authors['Author_Name']):
        author_dict[name] = index

    #genre_dict = getGenreDict(df_books['Genre_Name'], mydb)
    #getUserGenre(mydb)
    #df_books['Genre_Name'].value_counts().to_csv('dane.txt')
    main_data_array = []
    genre_data_array = []
    #0 'Name', 1'Author_Name', 2'Rating', 3' Description', 5 'Genre_Name', 6'NumberReviews', 7 'ImgSource'
    book_id = 0
    book_array = []

    for (index, data) in df_books.iterrows():
        if not data.isnull().values.any() :
            data_books = list(data)
            if data_books[0] not in book_array:
                if ' (Goodreads Author)' in data_books[1]:
                    data_books[1] = data_books[1].replace(' (Goodreads Author)','')
                    id_of_author = author_dict[str(data_books[1])]
                else:
                    id_of_author = author_dict[str(data_books[1])]
                des = re.sub(r'[^\x00-\x7f]',r' ',data_books[3])
                main_data_array.append((data_books[0], np.random.randint(16, size=1)[0], des, data_books[2], data_books[6], data_books[7], int(id_of_author)))
                book_id += 1 
                book_array.append(data_books[0])
            else:
                id_of_genre = genre_dict[str(data_books[5])]
                genre_data_array.append((int(book_id), int(id_of_genre)))
    
    df_main = pd.DataFrame(main_data_array, columns=['Name', 'Availability', 'Description', 'Rating', 'NumberReviews', 'ImgSource', 'Author_id'] )
    print(df_main.head(10))

    df_genres = pd.DataFrame(genre_data_array, columns =['Book_ID_id', 'Genre_ID_id'])
    print(df_genres.head(10))
    #df_main.to_csv("tmp.csv")
    df_main.to_sql(name='base_book_tmp', con=mydb, if_exists = 'append', index=False)
    df_genres.to_sql(name='base_bookgenres_tmp', con=mydb, if_exists = 'append', index=False)
    print("done")
readDataExcel()
