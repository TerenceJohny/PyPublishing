import custom_functions
import os
import streamlit as st
#from streamlit import session_state

file_path = os.path.join(os.path.dirname(__file__), 'todos.txt')

todos = custom_functions.get_todos(file_path)

st.title("ToDo App")
st.subheader("This is my webapp")
st.write("This app to increase your productivity")

def add_todo():
        to_do = st.session_state['new_todo'] + '\n'
        todos.append(to_do)
        custom_functions.write_todos(file_path, todos)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        custom_functions.write_todos(file_path, todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo" )
#st.session_state







