#!/usr/bin/python3
"""Defines  JSON file-reading fxn."""
import json


def load_from_json_file(filename):
    """Reads a Json_string from a JSON file
      while converting to a Python object

    Args:
        filename (str):  path of the file.

    Returns:
        any: read Python object
    """
    with open(filename) as f:
        return json.load(f)
