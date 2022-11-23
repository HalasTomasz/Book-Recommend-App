from GetData import * 
from K_means import *
from TFIDF_Alg import *
from nltk.tokenize import word_tokenize
# def cov_of_genre(genre_df, foreign_list):
#     return [ len(set(x).intersection(foreign_list)) / len(foreign_list) for x in genre_df ] 

if __name__ == "__main__":

   
    # s = '''Good muffins cost $3.88\nin New York's.  Please buy me.. two of them.\n\nThanks.'''
    # print(word_tokenize(s))
    books, booksDes, booksGenre = GetDataBooks() # Get DF here
    users, usersHistory, userWantednBooks, usersGenre = GetDataUsers()
    suggestUserTFIDF(usersHistory, booksDes)
    # print("staring")
    #suggestUserKMeans(usersHistory, books, usersGenre, booksGenre, userWantednBooks)
    # a = booksGenre.groupby('Book_ID').agg(sum)
    # print(a.head())
    # booksGenre = booksGenre.drop(tmp2)
    # out = booksGenre.groupby('Book_ID').agg(lambda col: col.tolist())
    # out = out.sort_values(by="Book_ID",ascending=False, key=lambda x: cov_of_genre(out['Genre_ID'],tmp))
    # print(out.index)
    # print("GOT")
    # TheBestAuthors(books)
    # TheMostRatedBooks(books)
    # AvgRating(books)
    # KMeanAlgortihm(books)
    #Run Allogiritms
    #print(usersHistory.groupby('Reader_ID').apply(lambda x : x.to_numpy().tolist() if not x.isnull().any()[0] else []).to_dict())

