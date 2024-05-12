import streamlit as st
import pandas as pd
from U_create import validate_user
from U_create import check_user_exists
from U_create import register

st.title("欢迎来到图书推荐系统!👋 ")
user_data = pd.read_csv('user-secret.csv')


user_name = st.text_input("*用户名* 👇👇👇")
secret = st.text_input("*密码* 👇👇👇")


if st.button("🛫登录"):
    if user_name != "" and secret != "":
        if validate_user(user_name, secret):
            st.session_state['user'] = user_name
            st.switch_page("pages/choose_page.py")
        else:
            st.write('用户名或密码错误！')
    else:
        st.write('请不要输入没有意义的的用户名或密码！')

if st.button("💳注册"):
    if user_name != "" and secret != "":
        exists = check_user_exists(user_name)
        if exists:
            st.write('用户名已存在，请换一个名字！')
        else:
            register(user_name, secret)
            st.write('注册成功！请重新登录。')
    else:
        st.write('请不要输入没有意义的的用户名或密码！')









