#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
defines all common attributes/methods for other classes:
"""


class BaseModel:
    """Define the BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
             models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        Dict = self.__dict__.copy()
        Dict['__class__'] = self.__class__.__name__
        Dict['created_at'] = self.created_at.isoformat()
        Dict['updated_at'] = self.updated_at.isoformat()
        return Dict

    def __str__(self):
        """Provides a readable string representation of the instance,"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
