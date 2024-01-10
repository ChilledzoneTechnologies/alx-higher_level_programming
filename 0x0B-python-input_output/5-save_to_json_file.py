#!/usr/bin/python3
"""Defines  JSON file-writing fxn."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object in the JSON file

    Args:
        my_obj (_type_):  object to be  saved in the JSON file
        filename (str):  path of the file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
