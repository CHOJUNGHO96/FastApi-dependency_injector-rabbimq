import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="node1", port=5672, credentials=pika.PlainCredentials("admin", "admin")))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f" [x] 수신완료: {message}")


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

try:
    print(' [*] 메세지 수신 대기중... 종료하려면 CTRL+C를 누르시오')
    channel.start_consuming()
except:
    print(" [*] 종료")
    channel.stop_consuming()
