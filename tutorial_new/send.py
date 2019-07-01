import pika

credentials = pika.PlainCredentials('one_user', 'qwertyui') # login + pass

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.142.0.2', port=5672, credentials=credentials)) # host, port and login+pass
channel = connection.channel()

print('OK!')
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', # default exchange
                      routing_key='hello', # название очереди
                      body='Hell !')
print(" [x] Sent 'Hello World!")


connection.close()