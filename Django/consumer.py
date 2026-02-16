import pika,json

params = pika.URLParameters('amqps://suspwcof:9S7bJRumZtF84e6A2bjMJjlFB5ONYyqD@chameleon.lmq.cloudamqp.com/suspwcof')

channels = pika.BlockingConnection(params).channel()


channels.queue_declare('main')

def callback(ch, method, properties, body):
    print(method,properties,body)

channels.basic_consume(queue='main', on_message_callback=callback,auto_ack=True)  
 
channels.start_consuming() 

channels.close()