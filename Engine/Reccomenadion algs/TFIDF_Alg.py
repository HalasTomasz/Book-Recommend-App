import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.corpus import stopwords
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
import re

not_added = set()
not_added_true = set()

def use_Natural_Leng(df_des):
 

    get_lower_letters = df_des.lower()
    get_lower_letters = re.sub('[^a-zA-Z0-9 \n\.]', ' ', get_lower_letters)
    get_lower_letters = get_lower_letters.replace('.', ' ')
    word_tokenaizer = nltk.word_tokenize(get_lower_letters)
    word_tager = nltk.pos_tag(word_tokenaizer)
    Penn_Treebank_tagset= ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] 
    forbiden_tag = ['CC','DT','PDT', 'PRP', 'SYM' , 'TO'] 
    lemmatizer = WordNetLemmatizer()
    stop_words_en = stopwords.words('english')
    
    out_list = [] 
    for i, word in enumerate(word_tokenaizer):
   
        if word_tager[i][1] in Penn_Treebank_tagset: # For Vebrs
            lemmatized = lemmatizer.lemmatize(word, 'v')
        else:
            lemmatized = lemmatizer.lemmatize(word)

        # if word_tager[i][1] in forbiden_tag  :
        #     not_added_true.add(str(word))
        #     not_added.add(str(word) + " " + str(name))
        #     continue

        if lemmatized not in stop_words_en and lemmatized.isalpha():
            if len(lemmatized) > 1:
                out_list.append(lemmatized)
        # else:
        #     not_added_true.add(str(word))
        #     not_added.add(str(word) + " " + str(name))
  
    des_filter = ' '.join(out_list)
    des_filter = des_filter.replace("'s", " is")
    des_filter = des_filter.replace("'m", " am")
    des_filter = des_filter.replace("'re", " are")
    des_filter = des_filter.replace("'ll", " will")
    des_filter = des_filter.replace("'ve", " have")
    des_filter = des_filter.replace("'d", " would")

    return des_filter
  

def TFIDF_Alg(books_df):

    #books_df["des_NN"] = [use_Natural_Leng(x, y) for (x,y) in zip(books_df['Des'], books_df.index)]
    books_df["des_NN"] = [use_Natural_Leng(x) for x in books_df['Des']]
    TfidfVec = TfidfVectorizer(encoding="UTF-8", dtype=np.float32)
    tf_idf =  TfidfVec.fit_transform(books_df['des_NN'])
    cos_sim = cosine_similarity(tf_idf, tf_idf)
    
    return cos_sim

def suggestUserTFIDF(user_history_df, books_des_df):

    cos_sim = TFIDF_Alg(books_des_df)
    tfidf_result = []
    user_hist_dict = user_history_df.groupby('Reader_ID').apply(lambda x : x.to_numpy().tolist()).to_dict()
    similarity_scores = []
    for array in cos_sim:
        tmp = pd.Series(array).sort_values(ascending = False)
        similarity_scores.append(list(tmp.iloc[1:8].index))

    del cos_sim
    #similarity_scores = pd.Series(cos_sim[1]).sort_values(ascending = False)
    #similarity_scores = pd.Series(cos_sim[32]).sort_values(ascending = False)
    #similarity_scores = [pd.Series(cos_sim[1]).sort_values(ascending = False) for array in]
    #  print(list(similarity_scores.iloc[1:15].index))
    # print(cos_sim[1][32])
    # print(cos_sim[32][1])

    #user_hist_dict = user_history_df.groupby('Reader_ID').apply(lambda x : x.to_numpy().tolist()).to_dict()
    #for user_id, lend_data in user_hist_dict.items():
    #books_history_ids = [int(book_details[-1]) - 1 for book_details in lend_data]
    for user_id, lend_data in user_hist_dict.items():
        books_history_ids = [int(book_details[-1]) - 1 for book_details in lend_data]
        books_history_ids_set = set(books_history_ids)
        result_arr = []
        for book_id in books_history_ids_set:
            result_arr.extend(similarity_scores[book_id])
        #print('Suggestion: K ', Kmeans_result_list, "Random: "  ,same_genre_book_list ,' For user ',user_id)
        print(user_id)
        result = list(set(result_arr) - books_history_ids_set)[:18]
        for user_rec in result:
            tfidf_result.append([2,user_rec+1, user_id])
    return tfidf_result
    # similarity_scores = pd.Series(cos_sim[1,2,3,4,5]).sort_values(ascending = False)
    # print(similarity_scores)

def SurveyTestingTFiDF(modified_books_df_index, books_des_df, books_df):
    cos_sim = TFIDF_Alg(books_des_df)
    similarity_scores = [pd.Series(array).sort_values(ascending = False) for array in cos_sim]
    answer = [] 
    print("Satring working")
    for index in modified_books_df_index:
        answer.append([similarity_scores[index].iloc[1:6].index])
    pd.options.display.max_colwidth
    x = 0
    with open("out1.2txt", "w", encoding='UTF-8') as f: 
        for ids_arr in answer:
            f.write(f"\'{books_df.iloc[modified_books_df_index[x]]['Name']}\':[")
            for el in ids_arr:
                print(el)
                f.write(f"\'{list(books_df.iloc[el]['Name'])}\',")
              
            f.write(f"]\n")
            x = x + 1
    print(answer)
    # minus 