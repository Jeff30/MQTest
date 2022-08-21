import pika
import sys


host = '192.168.0.146'
port = 5672
credentials = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host, port,'/'))
channel = connection.channel()
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body=message)

print(" [x] Sent %r" %message)
connection.close()