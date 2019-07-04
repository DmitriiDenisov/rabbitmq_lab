import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))  # sleep as many seconds as many pointers in received body
    print(" [x] Done")
    ch.basic_ack(
        delivery_tag=method.delivery_tag)  # Answer to RabbitMQ that all is successful => Message is marked as acknowledged


channel.queue_declare(queue='task_queue', durable=True)  # if not exists

# if next row is commented => even messages are transferred to consumer_1, odd to consumer_2
# This row allows to avoid idle of consumers: once a consumer is free it receives next message
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue',  # name of queue
                      # auto_ack=True, # True => if python crashes => do not send message back to queue
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
