import numpy as np 
import pandas as pd
import seaborn as sns
import isbnlib
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq
from pylab import plot, show
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from itertools import chain
from sklearn.metrics import silhouette_score


def TheBestAuthorsPlot(book_df):
    #Max number of books published by authors
    booking_counter = book_df.groupby('Author_Name')['Name'].count().reset_index().sort_values('Name', ascending=False).head(15)
    ax = sns.barplot(data=booking_counter, x= booking_counter['Name'],y=booking_counter['Author_Name'], palette='bright')
    ax.set_title("Top 15 Authorów z największa ilością książek")
    ax.set_xlabel("Liczba książek")
    ax.set_ylabel("Autor")
    for i in ax.patches:
        ax.text(i.get_width()+.3, i.get_y()+0.3, str(round(i.get_width())), fontsize = 10, color = 'k')
    plt.show()

def TheMostRatedBooksPlot(book_df):
    #Top 20 Highest Rated Books
    most_rated_books_counter = book_df.sort_values('NumberReviews', ascending = False).head(15)
    #plt.figure(figsize=(15,10))
    ax = sns.barplot(data=most_rated_books_counter, x= most_rated_books_counter['NumberReviews'], y=most_rated_books_counter['Name'], palette='bright')
    ax.set_title("Top 20 Highest Rated Books")
    ax.set_xlabel("Total Rates")
    for i in ax.patches:
        ax.text(i.get_width()+.3, i.get_y()+0.3, str(round(i.get_width())), fontsize = 10, color = 'k')
    plt.show()

def AvgRatingPlot(book_df):

    fig, ax = plt.subplots(figsize=[15,10])
    sns.distplot(book_df['Rating'],ax=ax)
    ax.set_title('Average rating distribution for all books',fontsize=20)
    ax.set_xlabel('Average rating',fontsize=13)
    plt.show()

def IneritaPlot(books_df):

    data = np.asarray([np.asarray(books_df['Rating']), np.asarray(books_df['NumberReviews'])]).T
    distortions = []
    for k in range(2,30):
        k_means = KMeans(n_clusters = k)
        k_means.fit(data)
        distortions.append(k_means.inertia_)

    plt.figure(figsize=(15,10))
    plt.plot(range(2,30), distortions, 'bx-')
    plt.title("Elbow Curve")
    
def KMeanAlgortihm(books_df):

    books_df['Ratings_Dist'] = segregate_rating(books_df) #Here we segregate boosk depepding on their avg rank  
    books_data = pd.concat([books_df['Ratings_Dist'].str.get_dummies(sep=","), books_df['Rating'], books_df['NumberReviews']], axis=1)
    minMaxScaler = MinMaxScaler()
    books_algo = minMaxScaler.fit_transform(books_data)
    np.round(books_algo, 3)
    model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
    model.fit(books_algo)
    _, indices = model.kneighbors(books_algo)

    return indices

def add_user_wanted_books(user_id, users_wanted_books_df):
    books = users_wanted_books_df.iloc[user_id]
    return len(books), books

def add_random_books(rest_number, user_genre_list, books_genre_df, read_books):
    if user_genre_list:
        genre_list = books_genre_df.drop(read_books).sort_values(by="Book_ID",ascending=False, key=lambda x: books_genre_df(books_genre_df['Genre_ID'],user_genre_list))[:rest_number-2]
        random_list = books_genre_df.drop(read_books).sample(n = 2).index
        return genre_list+ random_list
    else:
        return books_genre_df.drop(read_books).sample(n = rest_number).index



def suggestUserKMeans(user_history_df, books_df, user_genre_df, books_genre_df , users_wanted_books_df):

    number_of_rec = 18 
    indices = KMeanAlgortihm(books_df)  
    user_hist_dict = user_history_df.groupby('Reader_ID').apply(lambda x : x.to_numpy().tolist() if not x.isnull().any()[0] else [] ).to_dict()
    for user_id, lend_data in user_hist_dict.items():
        Kmeans_result_list = []
        books_history_ids = [] 
        if lend_data:
            books_history_ids = [int(book_details[-1]) for book_details in lend_data]
            books_history_ids_set = set(books_history_ids)
            ids = indices[books_history_ids]
            set_of_results = set(chain.from_iterable(ids))
            print(set_of_results - books_history_ids_set )
            Kmeans_result_list = list(set_of_results - books_history_ids_set)[:14]
            # minus 
        res_rec = number_of_rec - len(Kmeans_result_list)
        #books_number, Wanted_books_list = add_user_wanted_books(user_id, users_wanted_books_df)
        #user_genre_df.loc[[user_id]]
        same_genre_book_list = add_random_books(res_rec,[],books_genre_df, books_history_ids)
        print(len(books_genre_df))
        # result = Kmeans_result_list + same_genre_book_list
        print('Suggestion: K ', Kmeans_result_list, "Random: "  ,same_genre_book_list ,' For user ',user_id)
        
# def get_index_from_name(name):
#     return df[df["title"]==name].index.tolist()[0]

# def get_id_from_partial_name(partial):
#     for name in all_books_names:
#         if partial in name:
#             print(name,all_books_names.index(name))

            
def segregate_rating(data):
    segregation_array = []
    for rating in data.Rating:
        if rating>=0 and rating<=1:
            segregation_array.append("0-1")
        elif rating>1 and rating<=2:
            segregation_array.append("1-2")
        elif rating>2 and rating<=3:
            segregation_array.append("2-3")
        elif rating>3 and rating<=4:
            segregation_array.append("3-4")
        elif rating>4 and rating<=5:
            segregation_array.append("4-5")
        else:
            segregation_array.append("NaN")
    return segregation_array