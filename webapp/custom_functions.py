def get_todos(filepaths):
     with open(filepaths, 'r') as file_local: # shadows warning for variables from main scope
        todo_local = file_local.readlines()
        return todo_local

def write_todos(filepaths, todolist_arg):
    """
    write the todolist into filepath
    :param filepaths:
    :param todolist_arg:
    :return:
    """
    with open(filepaths, 'w') as file_local: # shadows warning for variables from main scope
        file_local.writelines(todolist_arg)
    #return todolist_arg
#print(__name__)
print(f"sourcing module:{__name__} \n \n ")
if __name__ == "__main__": ##__name__
    # is a variable that has the value "__main__" in the function
    # but when called from a main program as a
    # function ist value is the name of the function module
        print(f"Hello {__name__}")

