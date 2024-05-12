import streamlit as st
import userIO


def display_images_with_selectboxes(books_df):

    user_data = userIO.read()

    options = ["Rate", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    num_cols = 5  # Adjust the number of columns as needed
    num_rows = (len(books_df) + num_cols - 1) // num_cols  # Calculate rows dynamically

    # Create a container for multi-line layout
    with st.container():

        for row_index in range(num_rows):
            cols = st.columns(num_cols)

            for col_index, (_, book) in enumerate(books_df.iloc[row_index * num_cols: (row_index + 1) * num_cols].iterrows()):

                with cols[col_index]:
                    image_url = book.iloc[2]
                    book_title = book.iloc[1]
                    isbn = book.iloc[0]

                    st.caption("\n")

                    selection = st.selectbox(f"{col_index + 1 + row_index * num_cols}", options, key=isbn, label_visibility="collapsed")

                    st.image(image_url )

                    user_index= user_data[user_data['ISBN'] == str(isbn)].index

                    if selection != "Rate":
                        userIO.write(user_data,  str(isbn), int(selection), True)

                    # 显示评分记录
                    if user_data.loc[user_index, 'bool'].values[0] == False :
                        c = None
                        st.write(c)
                    else:
                        st.write(user_data.loc[user_index, 'rating'].values[0])

                    st.caption("ISBN:" + str(isbn))
                    st.caption(book_title)
                    st.caption("\n")





                    #print(selection)

