import streamlit as st
import pandas as pd
import pickle
import requests



def fetch_poster(movie_id):
    """
    this fuction fetch the poster detail from tmdb website
    """
    url = "https://api.themoviedb.org/3/movie/{}?api_key={Enter your own tndb api key}".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    """
    this function give us recommendation of the movie .
    this take movie name as input
    recommend 10 movies base on search

    """

    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:11]
    recommended_movie_names = []
    recommended_movie_poster = []
    for i in movie_list:
        recommended_movie_names.append(movies.iloc[i[0]].title)
        #fectch poster
        movieId = movies.iloc[i[0]].id
        recommended_movie_poster.append(fetch_poster(movieId))
    return recommended_movie_names ,recommended_movie_poster




st.title('Movie Recommender System')

# load pickle file this file have data of movies
movie_dict = pickle.load(open('movie_dict.pkl','rb'))

# load pickle file this file have vector distance of each movie 
similarity = pickle.load(open('similarity.pkl','rb'))

# convert data into DataFrame
movies = pd.DataFrame(movie_dict)

# create a dropbox
movie_list = movies['title'].values
selected_movie_name  = st.selectbox(
    "Type or select a movie from the dropdown",
   movie_list )



# create a buttton 
# make columns to show poster 
# this have 10 columns

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])