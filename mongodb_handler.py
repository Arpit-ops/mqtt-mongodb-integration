import pymongo
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MongoDBHandler:
    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_message(self, message):
        try:
            self.collection.insert_one(message)
            logger.info("Inserted message into MongoDB: %s", message)
        except Exception as e:
            logger.error("Error inserting message into MongoDB: %s", str(e))
