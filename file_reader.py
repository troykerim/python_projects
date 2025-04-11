'''
Read files from a folder
Verify that I have completed 50 projects (Complete BigBoxSWE's challenge)
'''

import os 


def read_files(folder_path):
    """Counts and prints the number of .py files in a specified folder

    Args:
        folder_path: The path to the folder containing the files.
    """
    try:
        py_files = [f for f in os.listdir(folder_path)
            if f.endswith('.py') and os.path.isfile(os.path.join(folder_path,f))]
        print(f"The number of .py files in '{folder_path}' is {len(py_files)-1}")  # Minus 1 to ignore this python file
        if (len(py_files) >= 50):
            print(f"You have finished BigBoxSWE's Challenge! Continue to work hard!")
        else:
            print("You have less than 50 projects done, keep going!")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
folder_path = "/home/troy/python_projects"  # Replace with the actual path to your folder
read_files(folder_path)