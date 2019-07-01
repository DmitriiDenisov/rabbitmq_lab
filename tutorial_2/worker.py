import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag) # ответ о том, что успешно обработано => сообщение помечается как acknowledged

channel.queue_declare(queue='task_queue', durable=True) # if not exists, durable - чтобы не пропали сообщения и очереди при краше RabbitMQ

channel.basic_qos(prefetch_count=1) # чтобы если consumer проставивает, то задачи направлялись к нему. Если закомментить, то нечетные попадают к Consumer_1, а четные к Consumer_2
channel.basic_consume(queue='task_queue',
                      #auto_ack=True, # True => если упал, то заново не направлять сообщение в очередь
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

