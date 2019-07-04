import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)  # durable=True => in case RabbitMQ crashes all queues are saved
# ps. RabbitMQ doesn't allow you to redefine an existing queue with different parameters

message = ' '.join(sys.argv[1:]) or "Six message.........."
channel.basic_publish(exchange='',
                      routing_key='task_queue',  # name of queue
                      body=message,  # message to be sent
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent, i.e. if RabbitMQ crashes this message is saved
                      ))
print(" [x] Sent %r" % message)

connection.close()
