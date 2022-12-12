import numpy as np 
import pandas as pd
import seaborn as sns
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
from scipy.stats import norm, kstest
from statistics import variance
import statsmodels.api as sm


def SurveyResult():

    pd.read_csv('./results/')
    
def TheBestAuthorsPlot(book_df):
    #Max number of books published by authors
    booking_counter = book_df.groupby('Author_Name')['Name'].count().reset_index().sort_values('Name', ascending=False).head(15)
    ax = sns.barplot(data=booking_counter, x= booking_counter['Name'],y=booking_counter['Author_Name'], palette="Set2")
    ax.set_xlabel("Liczba książek", fontsize=16)
    ax.set_ylabel("Autor" , fontsize=16)
    ax.legend(loc='best', fontsize=14)
    for i in ax.patches:
        ax.text(i.get_width()+.2, i.get_y()+0.2, str(round(i.get_width())), fontsize = 10, color = 'k')
    plt.show()

def TheMostRatedBooksPlot(book_df):
    #Top 20 Highest Rated Books
    most_rated_books_counter = book_df.sort_values('NumberReviews', ascending = False).head(15)
    #plt.figure(figsize=(15,10))
    ax = sns.barplot(data=most_rated_books_counter, x= most_rated_books_counter['NumberReviews'], y=most_rated_books_counter['Name'], palette="Set2")
    ax.set_xlabel("Liczba Ocen" , fontsize=16)
    ax.set_ylabel("Tytuł Książki" , fontsize=16)
    ax.legend(loc='best', fontsize=14)
    for i in ax.patches:
        ax.text(i.get_width()+.3, i.get_y()+0.3, str(round(i.get_width())), fontsize = 10, color = 'k')
    plt.show()

def AvgRatingPlot(book_df):

    fig, ax = plt.subplots(figsize=[15,10])
    sns.distplot(book_df['Rating'],ax=ax, kde=True, bins=22, label="Gęstośc empiryczna")
    ax.set_xlabel('Średnia ocena',fontsize=16)
    ax.set_ylabel("Gęstość",fontsize=16)
    EX = np.mean(book_df['Rating'])
    VarX = np.var(book_df['Rating'])
    x_range = np.arange(1.89, 5, 0.01)
    #print(1/( len(book_df['Rating']) -1)*sum([ pow(x - EX,2) for x in book_df['Rating']] ))
    # print(VarX)
    print(EX)
    print(variance(book_df['Rating']))
    y_range = norm.pdf(x_range, EX, np.sqrt(variance(book_df['Rating'])))
    plt.plot(x_range,y_range, label="Gęstośc teoretyczna")
    plt.legend()
    plt.show()  

def dist(book_df):
    fig, ax = plt.subplots(figsize=[15,10])
    x_range = np.arange(1.89, 5, 0.01)
    EX = np.mean(book_df['Rating'])
    y_range_ppf = norm.cdf(x_range, loc=EX, scale=np.sqrt(variance(book_df['Rating'])))
    print(y_range_ppf)
    sns.ecdfplot(book_df['Rating'], ax=ax, label="Dystrybuanta empiryczna")
    plt.plot(x_range, y_range_ppf, label="Dystrybuanta teoretyczna")
    ax.set_xlabel('Średnia ocena',fontsize=16)
    ax.set_ylabel("Wartość dystrybuanty",fontsize=16)
    plt.legend()
    plt.show()

def qqplots(book_df):
    fig, ax = plt.subplots(figsize=[15,10])
    EX = np.mean(book_df['Rating'])
    sm.qqplot(book_df['Rating'], dist= norm,line='45', ax=ax, loc=EX , scale=np.sqrt(variance(book_df['Rating'])))
    ax.set_xlabel('Teoretyczne kwantyle',fontsize=16)
    ax.set_ylabel("Empiryczne kwantyle",fontsize=16)
    plt.show()

    ks_statistic, p_value = kstest(book_df['Rating'], 'norm', args=(EX, np.sqrt(variance(book_df['Rating']))))
    print(ks_statistic, p_value)


def RelRevRatingsPlot(book_df):

   
    ax = sns.relplot(x="Rating", y="NumberReviews", data = book_df, color = 'red',sizes=(100, 200), height=7, marker='o' )
    ax.set_axis_labels("Średnia ocena","Liczba ocen", fontsize=16)
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()


def RelClasterPloter(book_df):


    data = np.asarray([np.asarray(book_df['Rating']), np.asarray(book_df['NumberReviews'])]).T
    centroids, _ = kmeans(data, 6)
    idx, _ = vq(data, centroids)
    plt.figure(figsize=(15,10))
    plt.scatter(data[idx==0,0],data[idx==0,1],c='red')
    plt.scatter(data[idx==1,0],data[idx==1,1],c='yellow')
    plt.scatter(data[idx==2,0],data[idx==2,1],c='darkgreen')
    plt.scatter(data[idx==3,0],data[idx==3,1],c='black')
    plt.scatter(data[idx==4,0],data[idx==4,1],c='blue')
    plt.scatter(data[idx==5,0],data[idx==5,1],c='olive')

    plt.scatter(centroids[:,0],centroids[:,1], c='indigo', marker='s',linewidths=5)

    plt.legend(['Klaster 1','Klaster 2', 'klaster 3', 'Klaster 4', 'Klaster 5', 'Klaster 6', 'Centroidy'], fontsize=16)
    plt.ylabel('Liczba ocen' ,fontsize=16)
    plt.xlabel('Średnia ocena',fontsize=16)
    plt.show()

def IneritaPlot(books_df):

    data = np.asarray([np.asarray(books_df['Rating']), np.asarray(books_df['NumberReviews'])]).T
    distortions = []
    for k in range(2,20):
        k_means = KMeans(n_clusters = k)
        k_means.fit(data)
        distortions.append(k_means.inertia_)

    plt.figure(figsize=(15,10))
    plt.plot(range(2,20), distortions, 'bx-')
    plt.title("Krzywa inercji")
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

def BookdsDesPlot(book_des_df):

     tmp_arr = [len(x) for x in book_des_df['Des'] if 30 < len(x) <= 4000]
     n, bins, patches = plt.hist(tmp_arr, bins=16)
     plt.ylabel('Liczba książek', fontsize=16)
     plt.xlabel('Liczba słów', fontsize=16)
     plt.xticks(bins)
     plt.show()
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

def cov_of_genre(genre_df, foreign_list):
    return [ len(set(x).intersection(foreign_list)) / len(foreign_list) for x in genre_df ] 

def add_random_books(rest_number, user_genre_list, books_genre_df, read_books):
    #print(books_genre_df.drop(read_books).sort_values(by="Book_ID",ascending=False, key=lambda x: books_genre_df(books_genre_df['Genre_ID'], user_genre_list)).sample(n = rest_number).index)
    books_genre_df = books_genre_df.drop(read_books)
    genre_list = books_genre_df.sort_values(by="Book_ID",ascending=False, key=lambda x: cov_of_genre(books_genre_df['Genre_ID'], user_genre_list))
    first_result = list(genre_list.index)[:2]
    second_result = list(genre_list.sample(rest_number-2).index)
    first_result.extend(second_result)

    return first_result
    


def suggestUserKMeans(user_history_df, books_df, user_genre_df, books_genre_df):

    number_of_rec = 18 
    indices = KMeanAlgortihm(books_df)
    kmeans_result = []  
    user_hist_dict = user_history_df.groupby('Reader_ID').apply(lambda x : x.to_numpy().tolist()).to_dict()
    #user_genre_list = user_genre_df.groupby('Reader_ID')['Genre_ID'] # Check this
    # Index from df is 0 
    # Where book index is + 1 
    for user_id, lend_data in user_hist_dict.items():

        books_history_ids = [int(book_details[-1]) - 1 for book_details in lend_data]
        books_history_ids_set = set(books_history_ids)
        ids = indices[books_history_ids]
        set_of_results = set(chain.from_iterable(ids))
        Kmeans_result_list = list(set_of_results - books_history_ids_set)[:14]
        res_rec = number_of_rec - len(Kmeans_result_list)
        print(user_id)
        books_history_ids_set.update(set_of_results)
        same_genre_book_list = add_random_books(res_rec, user_genre_df.iloc[user_id-1, 0], books_genre_df, list(books_history_ids_set))
        Kmeans_result_list.extend(same_genre_book_list)

        #print('Suggestion: K ', Kmeans_result_list, "Random: "  ,same_genre_book_list ,' For user ',user_id)
        for user_rec in Kmeans_result_list:
            kmeans_result.append([1,user_rec+1, user_id])
 
    return kmeans_result

def SurveyKMeans(modified_books_df_index, books_df):

    indices = KMeanAlgortihm(books_df)  
    ids = indices[modified_books_df_index]
    x = 0
    with open("out2.2.txt", "w", encoding='UTF-8') as f: 
        for ids_arr in ids:
            f.write(f"\'{books_df.iloc[modified_books_df_index[x]]['Name']}\':[")
            for el in ids_arr[1:]:
                f.write(f"\'{books_df.iloc[el]['Name']}\',")
            
            f.write(f"], \n")
            x = x + 1

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