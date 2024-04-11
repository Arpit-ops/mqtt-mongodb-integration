import unittest
from unittest.mock import MagicMock
from mongodb_handler import MongoDBHandler  # Import MongoDBHandler from your main script


class TestMessageProcessing(unittest.TestCase):
    def setUp(self):
        # Set up a mock MongoDBHandler instance for testing
        self.mongo_handler = MongoDBHandler("test_db", "test_collection")

    def test_insert_into_mongodb(self):
        # Test valid message insertion
        valid_message = {"sensor_id": "1", "value": 25.5}
        self.mongo_handler.collection.insert_one = MagicMock(return_value=True)
        self.assertTrue(self.mongo_handler.insert_message(valid_message), "Valid message failed insertion into MongoDB")

        # Test invalid message insertion
        invalid_message = {"sensor_id": "2"}  # Missing 'value' field
        self.mongo_handler.collection.insert_one = MagicMock(side_effect=Exception("Test error"))
        self.assertFalse(self.mongo_handler.insert_message(invalid_message),
                         "Invalid message passed insertion into MongoDB")


if __name__ == "__main__":
    unittest.main()
