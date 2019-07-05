#!/usr/bin/env python

# ----
# Examples of calls:
# python emit_log_direct.py error "Run. Run. Or it will explode."
# python emit_log_direct.py warning "Just warning"
# python emit_log_direct.py info "This is info message"
# python emit_log_direct.py Warning "import Warning"
# python emit_log_direct.py random_message "Hello world!"
# ----
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,  # for example error/warning/info
    body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
