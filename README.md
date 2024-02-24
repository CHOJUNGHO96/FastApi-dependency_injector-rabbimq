# FastApi + dependency_injector + rabbimq

This project is a reference implementation using FastAPI, Dependency Injector, and RabbitMQ.

## Installation and Execution

1. Ensure Docker and Docker Compose are installed.
2. Clone this repository: `git clone [GitHub Repository URL]`
3. Launch the services with the following command: `docker-compose up --build`
4. Find the FastAPI container ID using docker ps, and then connect with docker exec -it [container ID] /bin/bash
5. To run the consumer in the background, execute the command: poetry run python /app/background/receiver.py
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/5f55afc5-730f-4f62-ae74-2885689cb1e0)
6. Access the application in your browser at `localhost:8000/docs`.

## Execution Test

1. Enter a message and make an API request.
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/ded5bd94-54ec-448e-8b21-7fefdf585286)

2. The message gets queued. `127.0.0.1:15672`
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/f0db325f-afb5-4b44-a86b-adbf8ce68ed6)

3. When the consumer is run in the background, it subscribes to messages queued earlier.
<br/>![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/b9a11ca9-5036-4db4-b389-4b82474a8f2d)
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/98729b23-f9cb-41af-a2a7-58c34e60a9c3)


