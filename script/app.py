# import model
import pickle
import pandas as pd
import streamlit as st
from numpy.ma.core import mvoid

# load model
similarity_distance = pickle.load(open('model/similarity_distance.pkl', 'rb'))
data = pd.DataFrame(pickle.load(open('model/final_data.pkl', 'rb')))
################################################################################

# function which return 5 to similar movie name from data
def movie_recommend(movie_title_name: str) -> list:
    matching_movies = data.loc[data["title"] == movie_title_name]

    if matching_movies.empty:
        return [f"Sorry, '{name}' was not found in the database."]

    movie_index = matching_movies.index[0]
    distance = similarity_distance[movie_index]

    m_list = sorted(list(enumerate(distance)), key= lambda x : x[1], reverse=True)

    recommended_movie = []
    for val in m_list[1:6]:
        movie_title = data.iloc[val[0]].title
        recommended_movie.append(movie_title)
    return recommended_movie
###########################################################

# building the app
st.header("Movie Recommender")
movie_name = st.selectbox(label="Write the movie name", options=data["title"], placeholder="Enter movie name", index=None)


if movie_name:
    movie_list = movie_recommend(movie_name)
    st.subheader("The movie similar to it, that you will like it :)")
    for name in movie_list:
        st.write(name)
