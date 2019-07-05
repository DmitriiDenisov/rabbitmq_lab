#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout') # if it does not exists
# list of exchanges: 'sudo rabbitmqctl list_exchanges'

# queue='' => generate queue with random name
# exclusive=True => delete after connection is closed. In UI in column 'Features' is written 'Excl'
result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

# A binding is a relationship between an exchange and a queue. This can be simply read as: the queue is interested in messages from this exchange.
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, # listening to our temporary queue
    on_message_callback=callback,
    auto_ack=True)

channel.start_consuming()
