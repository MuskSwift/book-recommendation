import pandas as pd
import streamlit as st


def clean(sorted_result_df):
    username = st.session_state['user']
    user_ratings = pd.read_csv(f'users_rating_data/{username}.csv')
    bool_true_isbns = user_ratings[user_ratings['bool'] == 1]['ISBN']

    sorted_result_df = sorted_result_df.drop(bool_true_isbns, errors='ignore')

    return sorted_result_df
