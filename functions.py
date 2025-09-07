FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_locals:
        todos_locals = file_locals.readlines()
    return todos_locals

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

if __name__ == "__main__":
    print("This function is not meant to be run directly.")
    print("Please import it into your main application.")  