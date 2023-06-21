import os

def get_project_root():
    # Get the absolute path of the current file
    current_path = os.path.abspath(__file__)
    # Return the parent directory (project root)
    return os.path.dirname(os.path.dirname(current_path))

def check_if_file_exists():
    """
    this function is used to check if the file exists
    :param file_path: path of the file
    :return: True if file exists else False
    """
    root_path = get_project_root()
    return os.path.exists(f'{root_path}/vector_store.json')