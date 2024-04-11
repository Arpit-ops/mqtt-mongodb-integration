import pika
import json
import logging
import sys

import unittest
from mongodb_handler import MongoDBHandler
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MQTTHandler:
    def __init__(self, topics):
        self.topics = topics

    def process_message(self, channel, method, properties, body):
        try:
            message = json.loads(body)
            # Add your message processing logic here
            logger.info("Received and processed message: %s", message)
        except Exception as e:
            logger.error("Error processing message: %s", str(e))

    def start_consuming(self):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.exchange_declare(exchange='mqtt', exchange_type='topic')

            for topic in self.topics:
                queue_name = channel.queue_declare(queue='', exclusive=True).method.queue
                channel.queue_bind(exchange='mqtt', queue=queue_name, routing_key=topic)
                channel.basic_consume(queue=queue_name, on_message_callback=self.process_message, auto_ack=True)

            logger.info("Started consuming MQTT messages")
            channel.start_consuming()
        except Exception as e:
            logger.error("Error starting MQTT consumer: %s", str(e))
            sys.exit(1)


if __name__ == "__main__":
    # Run unit tests
    unittest.main()

    # MongoDB configuration
    mongo_handler = MongoDBHandler("your_database_name", "your_collection_name")

    # MQTT configuration
    mqtt_handler = MQTTHandler(["topic1", "topic2"])  # Add your MQTT topics here
    mqtt_handler.start_consuming()
