#!/usr/bin/python3
"""basic implementation of the FileStorage class"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects
    def __init__(self):
        FileStorage.__objects = {} 
    def new(self, obj):
        """Adds a new object to __objects with key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """doc doc"""
        path = FileStorage.__file_path
        objects = dict(FileStorage.__objects)
        for key, val in objects.items():
            objects[key] = val.to_dict()
        with open(path, 'w') as file:
            json.dump(objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
            except FileNotFoundError:
                print(f"File '{filepath}' not found.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON file '{filepath}': {e}")
