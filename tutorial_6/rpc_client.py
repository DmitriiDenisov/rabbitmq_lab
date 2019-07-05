#!/usr/bin/env python
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        # Create temporary queue for answer
        result = self.channel.queue_declare(queue='', exclusive=True)  # this is queue of publisher!
        self.callback_queue = result.method.queue

        self.channel.basic_consume(  # will listen to our temp queue in order to get answer
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:  # waiting for response from consumer with correlation_id
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',  # this is queue of Consumer !
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,  # send name of queue to which send an answer
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:  # endless loop for waiting for response
            self.connection.process_data_events()
        return int(self.response)  # print the response from consumer


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(7)")
response = fibonacci_rpc.call(7)  # Get request to server
print(" [.] Got %r" % response)  # Get answer from it
