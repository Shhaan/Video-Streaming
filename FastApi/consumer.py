import pika

params = pika.URLParameters('amqps://suspwcof:9S7bJRumZtF84e6A2bjMJjlFB5ONYyqD@chameleon.lmq.cloudamqp.com/suspwcof')

channels = pika.BlockingConnection(params).channel()


channels.queue_declare('hello')

def callback(ch, method, properties, body):
    print('recived message')
channels.basic_consume(queue='hello', on_message_callback=callback,auto_ack=True) 
print('start consuming') 
 
channels.start_consuming() 

channels.close()