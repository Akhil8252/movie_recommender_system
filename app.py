import streamlit as st
import pandas as pd
import pickle
import requests
st.title("Movie Recommender System")

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ddef881f7233f997538dee4042a2cda7".format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w185/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_poster_movies = []
    for i in movie_list:
        movie_id = movies.loc[i[0]].movie_id
        recommended_movies.append(movies.loc[i[0]].title)
        #fetch poster from API
        recommended_poster_movies.append(fetch_poster(movie_id))
    return recommended_movies,recommended_poster_movies

movies_dict = pickle.load(open(movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

searched_movie = st.selectbox('Enter the name of the movie?',movies['title'].values)


if st.button('Recommend'):
    names,posters = recommend(searched_movie)
    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])

