import streamlit as st
import pandas as pd

from func import display_images_with_selectboxes

books = pd.read_csv('info/top_10_books.csv')

user = st.session_state['user']

st.title(f"你好， {user}!")
st.write(':sunglasses: *请先给下面的书打分:* ')

display_images_with_selectboxes(books)

if st.button("🪄开始推荐"):
    st.switch_page("pages/recommendation_page.py")



