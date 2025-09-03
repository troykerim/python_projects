'''
Python script that accepts a JSON file, and will display the overall structure of the file.
'''

import json
import sys

def explore_json(obj, indent=0):
    # Recursively print the structure of a JSON object.
    
    # Creates an indention for each level of the json file we find
    prefix = "  " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{prefix}{k}")
            explore_json(v, indent + 1) # Recursive call, increment the indent counter
    # If the object is a list (JSON array)
    elif isinstance(obj, list):
        # Prints that it’s a list, and how many items it contains.
        print(f"{prefix}[list with {len(obj)} items]")
        if len(obj) > 0:
            explore_json(obj[0], indent + 1) 
    else:
        print(f"{prefix}{type(obj).__name__}")  # If the object is neither dict nor list, print its type

def main(json_path):
    # Load a JSON file and explore its structure.
    with open(json_path, "r") as f:
        data = json.load(f)
    explore_json(data)

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python3 json_explorer.py <path-to-your-json-file>")
        print("\nNOTE:")
        print("If your python is setup different on your computer, you have to run python instead of python3!")
        print("Additonally, you may have run: python3 json_explorer.py '<path-to-your-json-file>'")
    else:
        main(sys.argv[1])