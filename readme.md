# IoT Data Handling System

## Overview
The IoT Data Handling System is a backend application developed in Python that facilitates the ingestion, processing, and storage of MQTT messages from IoT devices. It integrates MQTT messaging with RabbitMQ for message queuing and uses MongoDB as the database for storing processed data. The system is designed to efficiently handle high volumes of messages, support various message types, and ensure data integrity throughout the process.

## Features
### MQTT and RabbitMQ Integration
- **RabbitMQ Configuration:** Configure RabbitMQ to handle MQTT messages by setting up the MQTT plugin.
- **MQTT Consumer:** Implement a Python service that connects to RabbitMQ and subscribes to specific MQTT topics.
- **Scalability:** Ensure the service can handle high volumes of messages and different message types efficiently.

### Message Processing
- **Message Parsing:** Develop logic in Python to parse incoming MQTT messages.
- **Validation:** Implement validation logic to ensure the integrity and validity of message content.
- **Transformation:** Perform any necessary transformations on message data to prepare it for storage.
- **Error Handling and Logging:** Implement robust error handling mechanisms and logging to manage any issues during message processing.

### MongoDB Integration
- **Schema Design:** Design an appropriate MongoDB schema to store processed MQTT messages. Consider the nature of IoT data for structuring the database.
- **Data Insertion:** Write Python scripts to insert processed messages into MongoDB, ensuring data integrity and efficiency in insertion and retrieval.

### Testing and Reliability
- **Unit Tests:** Create unit tests for Python code to validate the functionality of message processing and database operations.
- **Integration Tests:** Write integration tests to ensure the entire system (from MQTT message ingestion to MongoDB storage) works seamlessly.

## File Structure
- `main.py`: Contains the MQTTHandler class for MQTT message consumption.
- `mongodb_handler.py`: Contains the MongoDBHandler class for MongoDB connection and insertion operations.
- `test_message_processing.py`: Contains unit tests for message processing logic.
- `test_mongo_integration.py`: Contains integration tests for MongoDB operations.

## Usage
1. **Installation:** Install RabbitMQ, MongoDB, and Python dependencies (`pika`, `pymongo`) using the provided `requirements.txt`.
2. **Running the Application:** Execute `python mqtt_handler.py` to start consuming MQTT messages and storing them in MongoDB.
3. **Testing:** Optionally, run `python test_message_processing.py` and `python test_mongo_integration.py` to run unit and integration tests, respectively.

## Dependencies
- RabbitMQ: A message broker for handling MQTT messages.
- MongoDB: A NoSQL database for storing processed MQTT messages.
- Python: The programming language used for developing the backend system and running the scripts.

## Contributors
- Arpit joshi(https://github.com/yourusername): Description of contributions, if any.

## License
This project is licensed under the [MIT License](LICENSE).
