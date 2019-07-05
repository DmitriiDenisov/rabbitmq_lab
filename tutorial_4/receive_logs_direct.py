#!/usr/bin/env python

# ----
# Examples of runs:
# python receive_logs_direct.py info warning error
# python receive_logs_direct.py info warning error random_message
# python receive_logs_direct.py error
# ---

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')  # if it does not exist

result = channel.queue_declare(queue='', exclusive=True)  # temporary random queue which will listen to exchange
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:  # for each severity create binding (=edge) between queue and exchange
    channel.queue_bind(
        exchange='direct_logs',
        queue=queue_name,
        routing_key=severity  # each binding will listen to messages which routing_key will be equal to its severity
    )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
