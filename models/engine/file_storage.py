#!/usr/bin/python3
"""basic implementation of the FileStorage class"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    def __init__(self):
        self._file_path = os.path.join(os.getcwd(), "file.json")
        self._objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self._objects

    def new(self, obj):
        """Adds a new object to __objects with key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[key] = obj

    def save(self):
        """doc doc"""
        json_objects = {
                key: obj.to_dict()
                for key, obj in self._objects.items()
                }
        with open(self._file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        filepath = self._file_path
        self._objects = {}
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            self._objects[key] = BaseModel(**value)

            except FileNotFoundError:
                print(f"File '{filepath}' not found.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON file '{filepath}': {e}")
