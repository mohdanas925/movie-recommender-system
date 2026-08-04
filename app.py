import streamlit as st
import pandas as pd
import pickle

import os
import urllib.request

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(open(SIMILARITY_FILE, "rb"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

print(movies_list)

st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a Movie? ', movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)


SIMILARITY_FILE = "similarity1.pkl"

URL = "https://huggingface.co/datasets/mohdanas925/movie-recommender-files/resolve/main/similarity1.pkl"

if not os.path.exists(SIMILARITY_FILE):
    urllib.request.urlretrieve(URL, SIMILARITY_FILE)

