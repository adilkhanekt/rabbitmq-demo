import pika

def main():
    credentials = pika.PlainCredentials("adminuser", "adminuser")
    parameters = pika.ConnectionParameters("3.80.212.128", 5672, "/", credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue="queue1")

    while True:
        channel.basic_publish(exchange="", routing_key="queue1", body="Hello World!")
        print(" [x] Sent 'Hello world!' ")

    connection.close()

if __name__ == "__main__":
    main()

