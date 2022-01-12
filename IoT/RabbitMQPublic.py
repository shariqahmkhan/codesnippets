import pika, os

# set environment variable
url = os.environ.get("CLOUDAMQP_URL", "amqps://qrbymqes:WhDgpM8U7_GtVISPoEm8wZQ6BnJCJnMG@snake.rmq2.cloudamqp.com/qrbymqes")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare("test")
channel.queue_declare(queue= "test1")

# now bind queue and exchange
channel.queue_bind("test1", "test", "tests")

# publish
channel.basic_publish(

    body="hello",
    exchange = "test",
    routing_key="tests"    
    
    )

print("message sent")
channel.close()
connection.close()
