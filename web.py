
# import streamlit as st
# import functions



# todos = functions.get_todos("todos.txt")


# def add_todo():
#     todo = st.session_state["new_todo"]
#     todos.append(todo + "\n")
#     functions.write_todos(todos, "todos.txt")
#     st.session_state["new_todo"] = ""



# st.title("My to-do📃")
# st.subheader("Write to-do and stay productive")
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #4a5759;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# for index, todo in enumerate(todos):
#     check_box = st.checkbox(todo, key=todo)  
#     if check_box:
#         todos.pop(index)
#         functions.write_todos(todos)
#         del st.session_state[todo]
#         st.rerun()



# st.text_input(label="", placeholder="Add new to-do", key="new_todo",on_change= add_todo)

# with st.sidebar:
#     st.title("Menu")

import streamlit as st
import functions

# Sidebar navigation
with st.sidebar:
    st.title("Menu")
    menu_option = st.radio("Go to:", ["Home", "About"])

# Home Page (To-Do logic)
if menu_option == "Home":
    st.title("My to-do📃")
    st.subheader("Write to-do and stay productive")
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #4a5759;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    todos = functions.get_todos("todos.txt")

    def add_todo():
        todo = st.session_state["new_todo"]
        todos.append(todo + "\n")
        functions.write_todos(todos, "todos.txt")
        st.session_state["new_todo"] = ""

    for index, todo in enumerate(todos):
        check_box = st.checkbox(todo, key=todo)
        if check_box:
            todos.pop(index)
            functions.write_todos(todos, "todos.txt")
            del st.session_state[todo]
            st.rerun()

    st.text_input(label="", placeholder="Add new to-do", key="new_todo", on_change=add_todo)

# About Page
elif menu_option == "About":
    st.title("About")
    st.markdown(
        """
        ### Streamlit To-Do App
        This is a simple and interactive to-do application built with Streamlit.
        - Add, remove, and keep track of your daily tasks.
        - Boost your productivity with a clean interface.
        """
    )

    






