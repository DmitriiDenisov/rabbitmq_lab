#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# The 'fanout' exchange is very simple. As you can probably guess from the name, it just broadcasts all the messages it receives to all the queues it knows.
channel.exchange_declare(exchange='logs', exchange_type='fanout') # fanout - значит одновременно всем очередям выкидывается сообщение

message = ' '.join(sys.argv[1:]) or "info: HEEEE!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # название очереди
                      body=message)
print(" [x] Sent %r" % message)
connection.close()