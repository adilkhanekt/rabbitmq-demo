import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def main():
    credentials = pika.PlainCredentials("adminuser", "adminuser")
    parameters = pika.ConnectionParameters("3.80.212.128", 5672, "/", credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    channel.basic_consume(queue='queue1',
                      auto_ack=True,
                      on_message_callback=callback)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)