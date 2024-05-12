import pandas as pd
import streamlit as st

def read():
    username = st.session_state['user']
    dtypes = {
        'ISBN': str,
        'rating': int,
        'bool': bool
    }
    df = pd.read_csv(f"users_rating_data/{username}.csv", dtype=dtypes)

    return df


def write(df, isbn, rating, bool):
    username = st.session_state['user']
    index_to_modify = df[df['ISBN'] == isbn].index

    # 修改rating和bool的值
    df.loc[index_to_modify, 'rating'] = rating
    df.loc[index_to_modify, 'bool'] = bool

    # 将修改后的DataFrame保存为新的CSV文件
    df.to_csv(f"users_rating_data/{username}.csv", index=False)



