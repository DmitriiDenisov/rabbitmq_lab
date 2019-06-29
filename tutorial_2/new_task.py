import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True) # durable=True => даже при краше RabbitMQ все сообщеия + очередь сохранятся

message = ' '.join(sys.argv[1:]) or "Six message......"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent %r" % message)


connection.close()
