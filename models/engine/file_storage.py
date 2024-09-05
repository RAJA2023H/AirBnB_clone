#!/usr/bin/python3
"""basic implementation of the FileStorage class"""
import json
from models.base_model import BaseModel
import os
import models


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects with key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_objects = {
                key: obj.to_dict()
                for key, obj in self.__objects.items()
                }
        with open(self.__file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path
        to __objects, if it exists."""
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
            except Exception:
                pass
