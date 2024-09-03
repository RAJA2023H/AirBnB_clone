#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
"""
"""


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up for each test"""
        self.model = BaseModel()

    def test_init_default(self):
        """Test instance creation"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

        """Check if BaseModel has specific methods"""
        self.assertTrue(hasattr(self.model, 'save'))
        self.assertTrue(hasattr(self.model, 'to_dict'))
        self.assertTrue(hasattr(self.model, '__str__'))

        """ Test update """
        self.model.name = "My First Model"
        self.model.my_number = 89
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "my_number"))

    def test_init_from_kwargs(self):
         """Test initialization from kwargs"""
         data = {
                 'id': '1234',
                 'created_at': '2024-09-01T12:00:00.000000',
                 'updated_at': '2024-09-01T12:30:00.000000',
                 'name': 'Test Model'
                 }
         model = BaseModel(**data)
         self.assertEqual(model.id, '1234')
         self.assertEqual(model.name, 'Test Model')
         self.assertEqual(model.created_at, datetime.fromisoformat('2024-09-01T12:00:00.000000'))
         self.assertEqual(model.updated_at, datetime.fromisoformat('2024-09-01T12:30:00.000000'))
    def test_save(self):
        """Test save method updates updated_at attribute"""
        old_up = self.model.updated_at
        time.sleep(1)
        self.model.save()
        self.assertGreater(self.model.updated_at, old_up)
        self.assertNotEqual(
                self.model.updated_at, old_up, "should change after save()"
                )

    def test_to_dict(self):
        """Test to_dict method"""
        self.model.name = "Test Model"
        self.model.my_number = 123
        a_dict = self.model.to_dict()

        # Check that to_dict returns a dictionary with correct keys and values
        self.assertEqual(a_dict['__class__'], 'BaseModel')
        self.assertEqual(a_dict['name'], "Test Model")
        self.assertEqual(a_dict['my_number'], 123)
        self.assertEqual(
                a_dict['created_at'], self.model.created_at.isoformat()
                )
        self.assertEqual(
                a_dict['updated_at'], self.model.updated_at.isoformat()
                )
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)

    def test_str(self):
        """Test __str__ method"""
        expected_str = (
                f"[{self.model.__class__.__name__}] ({self.model.id}) "
                f"{self.model.__dict__}"
                )
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
