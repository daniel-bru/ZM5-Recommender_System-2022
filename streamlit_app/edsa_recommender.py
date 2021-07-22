"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from PIL import Image

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
##
import base64

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure

# Added libraries
import seaborn as sns
from wordcloud import WordCloud
_lock = RendererAgg.lock

# Data Loading
title_list = load_movie_titles(
    '~/unsupervised_data/unsupervised_movie_data/movies.csv')

# Creating dataframes
df_movies = pd.read_csv(
    '~/unsupervised_data/unsupervised_movie_data/movies.csv')
df_imdb = pd.read_csv(
    '~/unsupervised_data/unsupervised_movie_data/imdb_data.csv')
df_tags = pd.read_csv('~/unsupervised_data/unsupervised_movie_data/tags.csv')

# App declaration


def main():
    # Loading Company logo
    st.sidebar.image('resources/imgs/Company_logo-alt.png')
    # row1_space1, center_, row1_space2 = st.beta_columns((.5, 1, .2,))
    # with center_, _lock:

    #     file_ = open('resources/imgs/Company_logo.gif', "rb")
    #     contents = file_.read()
    #     data_url = base64.b64encode(contents).decode("utf-8")
    #     file_.close()
    #     st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True, )

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Movie Dataset Visualization",
                    "Solution Overview", "Project Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png', use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option', title_list[14930:15200])
        movie_2 = st.selectbox('Second Option', title_list[25055:25255])
        movie_3 = st.selectbox('Third Option', title_list[21100:21200])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i + 1) + '. ' + j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i + 1) + '. ' + j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    if page_selection == "Project Team":
        st.header('Our Amazing Team')
        st.write('A team of 6 passionate AI solutionists.')
        # First row of pictures

        col1, col2, col3 = st.beta_columns(3)
        Pic = Image.open('resources/imgs/Daniel_Pic.png')
        col1.image(Pic, caption="Daniel Bruintjies", width=150)
        col1.write('dmbruintjies@gmail.com')

        Pic = Image.open('resources/imgs/Sabelo_Pic.png')
        col2.image(Pic, caption="Sabelo Makhanya", width=150)
        col2.write('isabelomakhanya@gmail.com')

        Pic = Image.open('resources/imgs/Matthew_Pic.png')
        col3.image(Pic, caption="Matthew Rip", width=150)
        col3.write('matthewrip0@gmail.com')

        col4, col5, col6 = st.beta_columns(3)
        Pic = Image.open('resources/imgs/Rickie_pic.png')
        col4.image(Pic, caption="Rickie Mogale Mohale", width=150)
        col4.write('mogalerickie@gmail.com')

        Pic = Image.open('resources/imgs/Givenson_Pic.png')
        col5.image(Pic, caption="Givenson Mwandla", width=150)
        col5.write('gtmwandla@gmail.com')

        Pic = Image.open('resources/imgs/Akhona_Pic.png')
        col6.image(Pic, caption="Akhona Njeje", width=150)
        col6.write('Akhonanjeje@yahoo.com')

    if page_selection == "Movie Dataset Visualization":

        st.title("Movie Dataset Visualization")
        st.info("This page shows various visuals about Movies from the IMDb database")

        # Plot_Name = ["Popular Movie Genres","Top 20 Actors in most Movies",
        # "Top 20 Directors With The  Most Movies ","Top 20 Popular Play Plots","Popular Movie tags Wordcloud"]
        # plot_selection = st.radio("Please Select  A Visualisation plot ",Plot_Name)

        # st.write("")

        # if plot_selection == "Popular Movie Genres":
        plotviz = ["Please select", "-- Popular Movie Genres", "-- Top 20 Actors in most Movies",
                   "-- Top 20 Directors With The  Most Movies", "-- Top 20 Popular Play Plots", "-- Popular Movie Tags"]

        plot_selection = st.sidebar.selectbox("Select visualisation", plotviz)
        if plot_selection == "-- Popular Movie Genres":

            ################# Plot 1 ############
            # Create dataframe containing only the movieId and genres

            movies_genres = pd.DataFrame(
                df_movies[['movieId', 'genres']], columns=['movieId', 'genres'])
            # Split genres seperated by "|" and create a list containing the genres allocated to each movie
            movies_genres.genres = movies_genres.genres.apply(
                lambda x: x.split('|'))
            # Create expanded dataframe where each movie-genre combination is in a seperate row
            movies_genres = pd.DataFrame([(tup.movieId, d) for tup in movies_genres.itertuples(
            ) for d in tup.genres], columns=['movieId', 'genres'])

            fig1 = Figure()
            ax = fig1.subplots()
            sns.countplot(y="genres", data=movies_genres, order=movies_genres['genres'].value_counts(
                ascending=False).index, color='b', ec='red', alpha=0.9, ax=ax)
            ax.set_ylabel('Genre')
            ax.set_title('Popular Movie Genres')
            st.pyplot(fig1)
            st.write("")
            st.info(
                'The graph shows that people tend to enjoy certain movie genres such as drama  and comedy than musical movies')

        

            ################# Plot 2 ############
        if plot_selection == "-- Top 20 Actors in most Movies":
            movies_actor = pd.DataFrame(df_imdb[['movieId', 'title_cast']], columns=[
                                        'movieId', 'title_cast'])

            # Split title_cast seperated by "|" and create a list containing the title_cast allocated to each movie
            movies_actor = movies_actor[movies_actor['title_cast'].notnull()]
            movies_actor.title_cast = movies_actor.title_cast.apply(
                lambda x: x.split('|'))
            # Create expanded dataframe where each movie-tite_cast combination is in a seperate row
            movies_actor = pd.DataFrame([(tup.movieId, d) for tup in movies_actor.itertuples(
            ) for d in tup.title_cast], columns=['movieId', 'title_cast'])
            movies_actor = movies_actor.groupby(
                ['title_cast'])['movieId'].count().reset_index(name='Number of Movies')
            movies_actor = movies_actor.sort_values(
                by='Number of Movies', ascending=False)
            # Sececting the Top 20 actors in movies
            movies_actor = movies_actor .head(20)
            movies_actor = movies_actor.sort_values(
                by='Number of Movies', ascending=True)

            y_labels = movies_actor['title_cast']

            # Plot the figure.
            y_labels = movies_actor['title_cast']
            fig2 = Figure(figsize=(17, 12), dpi=85)
            ax = fig2.subplots()
            ax = movies_actor['Number of Movies'].plot(
                kind='barh', color='b', fontsize=17, edgecolor='red', xlim=[45, 84], width=.75, alpha=0.8, ax=ax)
            #sns.countplot(y='title_cast', data=movies_actor,order=movies_actor['title_cast'].value_counts(ascending=False).index,palette='deep',ax=ax)
            ax.set_ylabel('Name of Actor', fontsize=30)
            ax.set_xlabel('Number of movies featuring the actor', fontsize=30)
            ax.set_title('Top 20 Actors in most Movies ', fontsize=30)
            ax.set_yticklabels(y_labels)
            st.pyplot(fig2)
            st.write("")
            st.info(
                'Actors mostly liked by people tend to be featured in most movies')

            ################## Plot 3 ################################
        if plot_selection == "-- Top 20 Directors With The  Most Movies":

            # grouping the movies by the director and counting the total number of movies per director
            movies_director = pd.DataFrame(
                df_imdb[['movieId', 'director']], columns=['movieId', 'director'])
            movies_director = movies_director.groupby(
                ['director'])['movieId'].count().reset_index(name="count")
            movies_director = movies_director.sort_values(
                by='count', ascending=False)
            movies_director = movies_director .head(20)
            movies_director = movies_director.sort_values(
                by='count', ascending=True)

            y_labels = movies_director['director']
            # Plot the figure.
            fig3 = Figure(figsize=(18, 12), dpi=85)
            ax = fig3.subplots()
            ax = movies_director['count'].plot(
                kind='barh', color='b', edgecolor='red', width=.7, fontsize=16, xlim=[8, 30], alpha=0.9, ax=ax)
            ax.set_title(
                'Top 20 directors with the  most Movies from imdb database', fontsize=30)
            ax.set_xlabel('Number of Movies Directed', fontsize=30)
            ax.set_ylabel('Name of director', fontsize=30)
            ax.set_yticklabels(y_labels)
            st.pyplot(fig3)
            st.write("")
            st.info(
                'Directors that are mostly liked by people tend to release the most number movies')
            st.write("")
            st.info('Actors and directors are featured in most movies are likely to receive more resources  for them to improve on  their craft, and the more people will like their movies')


            ################## Plot 4 ################################
        if plot_selection == "-- Top 20 Popular Play Plots":

            movies_plot = pd.DataFrame(df_imdb[['movieId', 'plot_keywords']], columns=[
                                       'movieId', 'plot_keywords'])
            # Split play plot seperated by "|" and create a list containing the play plot allocated to each movie
            movies_plot = movies_plot[movies_plot['plot_keywords'].notnull()]
            movies_plot.plot_keywords = movies_plot.plot_keywords.apply(
                lambda x: x.split('|'))
            # Create expanded dataframe where each movie-play_plot combination is in a seperate row
            movies_plot = pd.DataFrame([(tup.movieId, d) for tup in movies_plot.itertuples(
            ) for d in tup.plot_keywords], columns=['movieId', 'plot_keywords'])
            movies_plot = movies_plot.groupby(['plot_keywords'])[
                'movieId'].count().reset_index(name="count")
            movies_plot = movies_plot.sort_values(by='count', ascending=False)
            movies_plot = movies_plot.head(20)
            movies_plot = movies_plot.sort_values(by='count', ascending=True)

            y_labels = movies_plot['plot_keywords']
            # Plot the figure.
            fig4 = Figure(figsize=(18, 12), dpi=85)
            ax = fig4.subplots()
            ax = movies_plot['count'].plot(
                kind='barh', color='darkblue', fontsize=17, edgecolor='r', width=.7, alpha=0.7, ax=ax)
            ax.set_title('Top 20 Popular Play Plots ', fontsize=30)
            ax.set_xlabel('Total Number of Play Plots', fontsize=30)
            ax.set_ylabel('Movie plot', fontsize=30)
            ax.set_yticklabels(y_labels)
            st.pyplot(fig4)
            st.write("")
            st.info(
                'The  graph show\'s that people tend to enjoy a movie with certain movie plots, such as love and nudity.')

            ###################### Plot 5 ##############################
        if plot_selection == "-- Popular Movie Tags":

            tags_2 = str(list(df_tags['tag']))

            wc = WordCloud(background_color="white", max_words=100,
                           width=1600, height=800, collocations=False).generate(tags_2)
            plt.imshow(wc)
            plt.axis("off")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.rcParams["axes.grid"] = False
            st.pyplot()


            ###################### Select ##############################

        if plot_selection == "Please select":
            st.error("Waiting for a selection from user...")


if __name__ == '__main__':
    main()
