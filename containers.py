from dependency_injector import containers, providers
import pika


class RabbitMQContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["api"])
    connection = providers.Singleton(
        pika.BlockingConnection,
        pika.ConnectionParameters(host="node1", port=5672, credentials=pika.PlainCredentials("admin", "admin"))
        )
