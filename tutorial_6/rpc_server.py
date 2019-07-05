#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    # After we got message and find fib(n) we publish it to
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,  # name of temp queue to send an answer
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),  # correlation_id of message
                     body=str(response)  # fib(n)
                     )
    ch.basic_ack(delivery_tag=method.delivery_tag)


# We might want to run more than one server process.
# In order to spread the load equally over multiple servers we need to set the prefetch_count setting.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
