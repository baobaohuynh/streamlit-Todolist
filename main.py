import streamlit as st
import functions

todos = functions.get_todos()


st.title("My To-do List")
st.write("This application will help you increasing your productivity!")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    clear_item()


def clear_item():
    st.session_state["new_todo"] = ""


for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new item...",
              on_change=add_todo, key='new_todo')