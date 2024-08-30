#!/usr/bin/python3
import uuid
from datetime import datetime


"""
defines all common attributes/methods for other classes:
"""

class BaseModel:
    """Define the BaseModel Class"""

    def __init__(self, id=None):
        """Initialize a new BaseModel instance."""
        
        if id is None:
            self.id = str(uuid.uuid4()) 
        
        else:
            self.id = id

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


    def __str__(self):
        """Provides a readable string representation of the instance,"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        Dict = self.__dict__.copy()
        Dict['__class__'] = self.__class__.__name__
        Dict['created_at'] = self.created_at.isoformat()
        Dict['updated_at'] = self.updated_at.isoformat()
        return Dict
