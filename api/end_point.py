from dependency_injector.wiring import inject, Provide
from fastapi import Depends, HTTPException
from main import app
from containers import RabbitMQContainer
import pika


# 메시지 발행 엔드포인트

@app.post("/")
@inject
def publish_message(message: str, rabbitmq_connection: pika.BlockingConnection = Depends(Provide[RabbitMQContainer.connection])):
    channel = rabbitmq_connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    return {"message": "전송완료"}
