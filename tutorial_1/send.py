import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', # default exchange
                      routing_key='hello', # name of queue
                      body='Hell !') # text we send to the queue
print(" [x] Sent 'Hello World!")


connection.close()
