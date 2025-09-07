import streamlit as st
import functions



todos = functions.get_todos("todos.txt")

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos, "todos.txt")
    st.session_state["new_todo"] = ""



st.title("My to-do📃")
st.subheader("Write your to-do and stay productive")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)  
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="", placeholder="Add new to-do", key="new_todo",on_change= add_todo)

with st.sidebar:
    st.title("Menu")
    






