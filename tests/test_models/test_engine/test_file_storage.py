#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def setUp(self):
        """Create a test instance of FileStorage"""
        self.storage = FileStorage()

    def test_all(self):
        """Test that all() returns an empty dictionary initially"""
        self.assertEqual(self.storage.all(), {})

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
        """Test that reload() loads instances from the file"""
        new_storage = FileStorage()
        loaded_instances = new_storage.all()
        loaded_instance1 = None
        for instance in loaded_instances:
            if instance.__class__ == instance1.__class__ and instance.id == instance1.id:
                loaded_instance1 = instance
                break

    def test_file_existance(self):
        """Test that the file exists after saving instances"""
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()

        # Check that the file exists
        self.assertTrue(os.path.exists("file.json"))

        # Check that the file is not empty
        self.assertGreater(os.path.getsize("file.json"), 0)
