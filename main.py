from mqhandler import RabbitMqHandler


def callback(channel, method, properties, body):
    print('ch={} type={}'.format(channel, type(channel)))
    print('method={} type={}'.format(method, type(method)))
    print('prop={} type={}'.format(properties, type(properties)))
    print('body={} type={}'.format(body, type(body)))


mq = RabbitMqHandler()
mq.connect()
mq.consume(callback=callback)