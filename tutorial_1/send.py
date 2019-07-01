import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', # default exchange
                      routing_key='hello', # название очереди
                      body='Hell !')
print(" [x] Sent 'Hello World!")


connection.close()
