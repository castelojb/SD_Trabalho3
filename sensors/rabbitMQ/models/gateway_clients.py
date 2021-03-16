import pika
import uuid
from models.setup import URL_GATEWAY, GATEWAY_SERVICES


class GatewayRpcClient:

    def __init__(self):

        self.connection = pika.BlockingConnection(
            pika.URLParameters(URL_GATEWAY))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def __call__(self, body):

        self.response = None

        self.corr_id = str(uuid.uuid4())

        self.channel.queue_declare(GATEWAY_SERVICES['Identificate'])

        self.channel.basic_publish(
            exchange='',
            routing_key=GATEWAY_SERVICES['Identificate'],
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),

            body=body)

        while self.response is None:
            self.connection.process_data_events()

        return self.response

    def kill(self):

        self.channel.close()


class GatewayBasicClient:

    def __init__(self, queue):

        self.queue = queue

    def make_conn(self):

        self.connection = pika.BlockingConnection(
            pika.URLParameters(URL_GATEWAY))

        self.channel = self.connection.channel()

    def __call__(self, payload):

        self.make_conn()

        self.channel.queue_declare(self.queue)

        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=payload
        )

        self.kill()

    def kill(self):

        self.channel.close()
