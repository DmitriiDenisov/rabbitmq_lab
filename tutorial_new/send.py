import pika

credentials = pika.PlainCredentials('one_user', 'qwertyui')  # login + pass
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='10.142.0.2',  # host, in Google Cloud Internal IP
        port=5672,  # port, usually 5672 or 15672
        credentials=credentials  # login + pass
    )
)
channel = connection.channel()

print('OK!')
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',  # default exchange
                      routing_key='hello',  # name of queue
                      body='Hell !')
print(" [x] Sent 'Hello World!")

connection.close()
