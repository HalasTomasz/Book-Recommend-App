import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.corpus import stopwords
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity

def use_Natural_Leng(df_des):

    get_lower_letters = df_des.lower()
    get_lower_letters = get_lower_letters.replace("\n", "")
    word_tokenaizer = nltk.word_tokenize(get_lower_letters)
    word_tager = nltk.pos_tag(word_tokenaizer)
    Penn_Treebank_tagset= ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] # Verbs
    forbiden_tag = ['CC','DT', 'POS', 'PP', 'PPZ' , 'SENT' , 'SYM' , 'TO'] 
    lemmatizer = WordNetLemmatizer()
    stop_words_en = stopwords.words('english')
    out_list = [] 
    for i, word in enumerate(word_tokenaizer):

        if word_tager[i][1] in Penn_Treebank_tagset: # For Vebrs
            lemmatized = lemmatizer.lemmatize(word, 'v')
        else:
            lemmatized = lemmatizer.lemmatize(word)

        if word_tager[i][1] in forbiden_tag  :
            continue  

        if lemmatized not in stop_words_en and lemmatized.isalpha():
            out_list.append(lemmatized)
            
    des_filter = ' '.join(out_list)
    des_filter = des_filter.replace("'s", " is")
    des_filter = des_filter.replace("'m", " am")
    des_filter = des_filter.replace("'re", " are")
    des_filter = des_filter.replace("'ll", " will")
    des_filter = des_filter.replace("'ve", " have")
    des_filter = des_filter.replace("'d", " would")
    return des_filter
  

def TFIDF_Alg(books_df):

    books_df["des_NN"] = [use_Natural_Leng(x) for x in books_df['Des']]
    books_df.to_csv('result2.csv')
    TfidfVec = TfidfVectorizer(encoding="UTF-8", dtype=np.float32)
    tf_idf =  TfidfVec.fit_transform(books_df['des_NN'])
    cos_sim = cosine_similarity(tf_idf, tf_idf)
    
    return cos_sim

def suggestUserTFIDF(user_history_df, books_df):

    cos_sim = TFIDF_Alg(books_df)
    similarity_scores = pd.Series(cos_sim[1]).sort_values(ascending = False)
   
    print(list(similarity_scores.iloc[1:15].index))
    similarity_scores = pd.Series(cos_sim[32]).sort_values(ascending = False)

    print(list(similarity_scores.iloc[1:15].index))
    print(cos_sim[1][32])
    print(cos_sim[32][1])
    # similarity_scores = pd.Series(cos_sim[72]).sort_values(ascending = False)
    # top_10_movies = list(similarity_scores.iloc[1:20].index)
    # print(top_10_movies)