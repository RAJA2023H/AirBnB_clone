#!/usr/bin/python3
import unittest                                                                                                                                              from models.base_model import BaseModel
from datetime import datetime
"""
"""
class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def setUp(self):
    """
    Set up for each test
    """
    self.model = BaseModel()

     def test_init(self):                                                                                                                                             """Test instance creation"""                                                                                                                                                                                                                                                                                              self.assertIsInstance(self.model, BaseModel)                                                                                                                 self.assertIsInstance(self.model.id, str)                                                                                                                    self.assertIsInstance(self.model.created_at, datetime)                                                                                                       self.assertIsInstance(self.model.updated_at, datetime)
                                                                                                                                                                      """Check if BaseModel has specific methods"""
         self.assertTrue(hasattr(self.model, 'save'))
         self.assertTrue(hasattr(self.model, 'to_dict'))
         self.assertTrue(hasattr(self.model, '__str__'))                                                                                                                                                                                                                                                                           """Test save method updates updated_at attribute"""                                                                                                          def test_save(self):
             old_updated_at = self.model.updated_at
             time.sleep(1)
             self.model.save()
             self.assertGreater(self.model.updated_at, old_updated_at)                                                                                                    self.assertNotEqual(self.model.updated_at, old_updated_at, "The updated_at should change after save()")
