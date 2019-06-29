import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    if properties.content_type == 'application/json':
        d = json.loads(body.decode())
        print(" [x] Received %r" % d)
    else:
        print(" [x] Received %r" % body.decode())

channel.queue_declare(queue='hello') # if not exists

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

