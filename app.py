import pickle
import streamlit as st
import pandas as pd
import requests

# ----------------------------
# Load data (ONLY ONCE)
# ----------------------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ----------------------------
# Fetch poster from TMDB
# ----------------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url)
        data = response.json()

        poster_path = data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Image"

        return "https://image.tmdb.org/t/p/w500/" + poster_path

    except:
        return "https://via.placeholder.com/500x750?text=Error"

# ----------------------------
# Recommendation function
# ----------------------------
def recommend(movie):
    recommended_movie_names = []
    recommended_movie_posters = []

    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']   
        recommended_movie_names.append(movies.iloc[i[0]]['title'])
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters
# ----------------------------
# Streamlit UI
# ----------------------------
st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    if len(recommended_movie_names) == 0:
        st.warning("No recommendations found")
    else:
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])