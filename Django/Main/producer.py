import pika,json

params = pika.URLParameters('amqps://suspwcof:9S7bJRumZtF84e6A2bjMJjlFB5ONYyqD@chameleon.lmq.cloudamqp.com/suspwcof')

channels = pika.BlockingConnection(params).channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channels.basic_publish(exchange='', routing_key='main', body=json.dumps(body),properties=properties) 