import streamlit as st
import pandas as pd
import re

from func import display_images_with_selectboxes

book_name = st.text_input("*在这里输入你想找的书名* 👇👇👇")

if st.button("🔍搜索"):
    st.session_state['search'] = book_name
    st.switch_page("pages/search_results_page.py")


df = pd.read_csv("info/book.csv")
bookname = st.session_state['search']

pattern = re.compile('.*'.join(map(re.escape, bookname)), re.IGNORECASE)
result = df[df['Book-Title'].str.match(pattern, na=False)]

result = result.head(15)

st.title("🔍搜索结果 :")


display_images_with_selectboxes(result)

if st.button("🔙返回推荐页面"):
    st.switch_page("pages/recommendation_page.py")