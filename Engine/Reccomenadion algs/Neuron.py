# data science imports
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt
import seaborn as sns

def movie_recommender(book_user_mat_sparse, user, num_neighbors, distances,indices ):

    number_neighbors = num_neighbors
    user_index = book_user_mat_sparse.columns.tolist()[user]
    results = []
    for book_id,_ in list(enumerate(book_user_mat_sparse.index)):

        if book_user_mat_sparse.iloc[book_id, user_index] == 0:

            sim_movies = indices[book_id].tolist()
            movie_distances = distances[book_id].tolist()

            if book_id in sim_movies:
                id_movie = sim_movies.index(book_id)
                sim_movies.remove(book_id)
                movie_distances.pop(id_movie) 

            movie_similarity = [1-x for x in movie_distances]
            movie_similarity_copy = movie_similarity.copy()
            nominator = 0

            for s in range(0, len(movie_similarity)):
                #print(book_user_mat_sparse.iloc[sim_movies[s], user_index])
                if book_user_mat_sparse.iloc[sim_movies[s], user_index] == 0:
                #print(movie_similarity_copy,number_neighbors - 1)
                    if len(movie_similarity_copy) == (number_neighbors - 1):
                        movie_similarity_copy.pop(s)
                    
                    else:
                        movie_similarity_copy.pop(s-(len(movie_similarity)-len(movie_similarity_copy)))
                        
                else:

                    nominator = nominator + movie_similarity[s]*book_user_mat_sparse.iloc[sim_movies[s],user_index]
          
            if len(movie_similarity_copy) > 0:
                if sum(movie_similarity_copy) > 0:
                    predicted_r = nominator/sum(movie_similarity_copy)
                
                else:
                    predicted_r = 0

            else:
                predicted_r = 0
                
            book_user_mat_sparse.iloc[book_id,user_index] = predicted_r

    print(results)
    print(book_user_mat_sparse.iloc[:,user_index].tolist())
    recommend_movies(book_user_mat_sparse, user_index, 7)
    

def recommend_movies(book_user_mat_sparse, user, num_recommended_movies):
  recommended_movies = []
  for m in book_user_mat_sparse[book_user_mat_sparse[user] == 0].index.tolist():

    index_df = book_user_mat_sparse.index.tolist().index(m)
    predicted_rating = book_user_mat_sparse.iloc[index_df, user]
    recommended_movies.append((m, predicted_rating))
  #print(recommended_movies)
  sorted_rm = sorted(recommended_movies, key=lambda x:x[1], reverse=True)
  
  print('The list of the Recommended Books \n')
  rank = 1
  for recommended_movie in sorted_rm[:num_recommended_movies]:
    
    print('{}: {} - predicted rating:{}'.format(rank, recommended_movie[0], recommended_movie[1]))
    rank = rank + 1

def prepare_data():

    #   df_movies = pd.read_csv(
    #     os.path.join(self.path_movies),
    #     usecols=['movieId', 'title'],
    #     dtype={'movieId': 'int32', 'title': 'str'})
    # df_ratings = pd.read_csv(
    #     os.path.join(self.path_ratings),
    #     usecols=['userId', 'movieId', 'rating'],
    #     dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

    df_books_ratings = pd.read_csv('user_data_ML.csv')
    df_books_cnt = pd.DataFrame(
        df_books_ratings.groupby('book_id').size(),
        columns=['count'])
    popular_books= list(set(df_books_cnt.query('count >= 4').index))  # noqa
    books_filter = df_books_ratings.book_id.isin(popular_books).values

    df_users_cnt = pd.DataFrame(
        df_books_ratings.groupby('user_id').size(),
        columns=['count'])
    active_users = list(set(df_users_cnt.query('count >= 5').index))  # noqa
    users_filter = df_books_ratings.user_id.isin(active_users).values
    print(users_filter)
    print(books_filter)
    df_books_filtered = df_books_ratings[books_filter & users_filter]
    print(df_books_filtered)
    # pivot and create movie-user matrix
    book_user_mat = df_books_filtered.pivot_table(index='book_id', columns='user_id', values='rating').fillna(0)
    # create mapper from movie title to index
    # hashmap = {
    #     movie: i for i, movie in
    #     enumerate(list(df_movies.set_index('movieId').loc[movie_user_mat.index].title)) # noqa
    # }
    # transform matrix to scipy sparse matrix
    book_user_mat_sparse = csr_matrix(book_user_mat.values)

    # clean up
    #del df_movies, df_movies_cnt, df_users_cnt
    #del df_ratings, df_ratings_filtered, movie_user_mat
    
    return book_user_mat, book_user_mat_sparse

def KNN():
    numberRecc = 8
    movie_rating_thres, user_rating_thres = 50, 50
    book_id = 10
    model  = NearestNeighbors(metric='cosine', algorithm='brute')
   # model.set_params(**{'n_neighbors': 2,'algorithm': 'brute','metric': 'cosine','n_jobs': -1})
    book_user_mat, book_user_mat_sparse = prepare_data()

    # raw_recommends = self._inference(
    #     self.model, movie_user_mat_sparse, hashmap,
    #     fav_movie, n_recommendations)
    # _inference(self, model, data, hashmap, fav_movie, n_recommendations):
    model.fit(book_user_mat_sparse)
    # get input movie index
    #print('You have input movie:', fav_movie)
    #idx = self._fuzzy_matching(hashmap, fav_movie)
    # inference
    print('Recommendation system start to make inference')
    print('......\n')
    print(book_user_mat_sparse.head())
    idx = [4,5]
    distances, indices = model.kneighbors(book_user_mat_sparse,n_neighbors=8)
    # get list of raw idx of recommendations
    raw_recommends = sorted(list(zip(indices[idx].squeeze().tolist(),distances[idx].squeeze().tolist())),key=lambda x: x[1][:0:-1])
    #movie_recommender(book_user_mat, 2, 8, distances, indices)
    print(raw_recommends)

    A = model.kneighbors_graph(book_user_mat_sparse)
    A = A.toarray()
    print(A)
KNN()