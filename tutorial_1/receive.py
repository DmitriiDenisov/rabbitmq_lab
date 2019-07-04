import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Function will be applied then message received
def callback(ch, method, properties, body):
    if properties.content_type == 'application/json':
        d = json.loads(body.decode())
        print(" [x] Received %r" % d)
    else:
        print(" [x] Received %r" % body.decode())


channel.queue_declare(queue='hello')  # declare queue just in case it does not exists

channel.basic_consume(queue='hello',  # name of queue
                      auto_ack=True, # if python crashes => do not send message back to queue
                      # delete message from queue immediately (without waiting for response from consumer)
                      on_message_callback=callback)  # function to be applied

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
