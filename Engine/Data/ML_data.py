import pandas as pd
import numpy as np 
ratings = pd.read_csv("ratings.csv")
users = ratings['user_id'].unique()


arr_of_data = []

users_dict_sex = {}
users_dict_age = {}
books_id = range(1,10000)
users = range(1,5000)

sex_arr = ['Man','Woman','No'] 
ages_arr = ["16", "26", "40", "60", "100","0"] 
        
np.random.seed(100)

for user in users:

    sex = np.random.rand()
    age = np.random.rand()

    if sex < 0.45:
        user_sex = sex_arr[0]
    elif 0.45 < sex < 0.9:
        user_sex = sex_arr[1]
    else:
        user_sex = sex_arr[2] 

    if age < 0.15:
        user_age = ages_arr[0]
    elif 0.15 <= age < 0.30:
       user_age = ages_arr[1]
    elif 0.3 <= age < 0.45:
        user_age = ages_arr[2]
    elif 0.45 <= age < 0.6:
       user_age = ages_arr[3]
    elif 0.75 <= age < 0.9:
       user_age = ages_arr[4]
    else:
        user_age = ages_arr[5]

    users_dict_sex[user] = user_sex
    users_dict_age[user] = user_age

for books in books_id:
    number_of_reviews = np.random.randint(1,10)
    users = np.random.randint(1,4999,size= number_of_reviews)

    for user in users:
        arr_of_data.append([books, user, users_dict_sex[user], users_dict_age[user], np.random.randint(1,5)])

print(len(arr_of_data))
print(arr_of_data[0])

pd.DataFrame(arr_of_data, columns=['book_id', 'user_id', 'sex', 'age', 'rating']).to_csv("user_data_ML.csv",index=False)