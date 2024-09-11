#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
import json
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def setUp(self):
        """Create a test instance of FileStorage"""
        self.storage = FileStorage()
        self.filepath = models.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up after tests by removing the JSON file if it exists."""
        try:
            os.remove(self.filepath)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all() returns an empty dictionary initially"""
        fs = FileStorage()
        self.assertEqual(fs.all(), {})

    def test_new(self):
        """Test that new() adds a new instance to the storage"""
        instance = BaseModel()
        self.storage.new(instance)
        self.assertIn(f"BaseModel.{instance.id}", self.storage.all())

    def test_save(self):
        """Test that save() saves the instance to the file"""
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        # Check that the instance is saved to the file
        with open("file.json", "r") as f:
            data = f.read()
            self.assertIn(instance.id, data)

    def test_reload(self):
        new = BaseModel()
        keyname = "BaseModel."+new.id
        self.storage.new(new)
        self.storage.save()
        models.storage.all().clear()
        models.storage.reload()
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[keyname],
                         models.storage.all()[keyname].to_dict())
