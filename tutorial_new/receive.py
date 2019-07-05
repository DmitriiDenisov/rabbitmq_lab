import pika
import json

credentials = pika.PlainCredentials('one_user', 'qwertyui')  # login + pass
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='10.142.0.2',  # host, in Google Cloud Internal IP
        port=5672,  # port, usually 5672 or 15672
        credentials=credentials  # login + pass
    )
)
channel = connection.channel()


def callback(ch, method, properties, body):
    if properties.content_type == 'application/json':
        d = json.loads(body.decode())
        print(" [x] Received %r" % d)
    else:
        print(" [x] Received %r" % body.decode())


channel.queue_declare(queue='hello')  # if not exists

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
