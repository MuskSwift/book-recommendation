import streamlit as st
import pandas as pd
import numpy as np

from func import display_images_with_selectboxes
from clean import clean

username = st.session_state['user']
book_name = st.text_input("*在这里输入你想找的书名* 👇👇👇")

if st.button("🔍搜索"):
    st.session_state['search'] = book_name
    st.switch_page("pages/search_results_page.py")

st.title(f"🤗这些是{username}可能喜欢的书:")

#--------------------推荐算法----------------------------------------

# 加载相似度矩阵
cosine_sim_df = pd.read_csv('info/cos.csv', index_col=0)   #cos.csv 是离线计算好的相似度矩阵，处理过程在项目“matrix”中

# 加载用户评分数据，并设置ISBN为索引
user_ratings_df = pd.read_csv(f'users_rating_data/{username}.csv')
user_ratings_df.set_index('ISBN', inplace=True)

# 提取评分向量
rating_vector = user_ratings_df['rating']
# 确保余弦相似度矩阵的索引和评分向量的索引完全一致
cosine_sim_df = cosine_sim_df.loc[rating_vector.index, rating_vector.index]
# 计算乘积
result_vector = np.dot(cosine_sim_df, rating_vector)
# 将结果转换为DataFrame
result_df = pd.DataFrame(result_vector, index=cosine_sim_df.index, columns=['pre'])
# 对喜好度向量元素进行降序排序
sorted_result_df = result_df.sort_values(by='pre', ascending=False)


# 清理已经评过分的书籍
sorted_result_df = clean(sorted_result_df)

# 获取排名前20的ISBN号,存入列表
top_isbn = sorted_result_df.head(20)
recommend_list = top_isbn.index.tolist()

# 加载书籍数据，显出应该推荐给用户的书
books_df = pd.read_csv('info/book.csv')
recommended_books = books_df[books_df['ISBN'].isin(recommend_list)]

#--------------------推荐算法----------------------------------------

display_images_with_selectboxes(recommended_books)

if st.button("🪄刷新推荐结果"):
    st.switch_page("pages/recommendation_page.py")
