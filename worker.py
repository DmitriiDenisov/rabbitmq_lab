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

channel.queue_declare(queue='hello') # if not exists

channel.basic_consume(queue='hello',
                      #auto_ack=True, # True => если упал, то заново не направлять сообщение в очередь
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

