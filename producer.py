import pika
host = '192.168.0.146'
port = 5672
credentials = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host, port,'/'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

print(" [x] Sent 'Hello World!")
connection.close()