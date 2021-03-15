import json
import time
from threading import Thread

from models.gateway_clients import GatewayRpcClient, GatewayBasicClient
from models.messages import *
from setup import StatusType, EquipmentType, QUEUES, GATEWAY_SERVICES


class Sensor:

    def __init__(self, ip, port, name, type_, queue):
        self.ip = ip
        self.port = port
        self.name = name
        self.type = type_
        self.queue = queue

        self.gateway_rpc_client = GatewayRpcClient()
        self.gateway_basic_client = GatewayBasicClient(queue)

        self.IdentificateClient()

    def EquipmentDiedClient(self):

        message = Id()

        request = json.dumps(message(
            self._id
        ))

        self.gateway_basic_client(request, GATEWAY_SERVICES['EquipmentDied'])

        self.gateway_basic_client.kill()

    def makeIdentification(self):
        message = Identification()
        return message(
            self.name, self.type, self.ip, self.port
        )

    def IdentificateClient(self):

        request = json.dumps(self.makeIdentification())

        response = self.gateway_rpc_client(request, self.queue)

        self.gateway_rpc_client.kill()

        self._id = response.value


class Smoke(Sensor):

    def __init__(self, ip, port, name):

        type_ = EquipmentType['SENSOR']

        queue = QUEUES['SMOKE_QUEUE']

        super().__init__(ip, port, name, type_, queue)

        self.temp = 10

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):

        message = Status()

        return message(
            StatusType['TURN_ON_OFF'], self.temp, self._id
        )

    def SendStatus(self, args):

        while True:
            stats = json.dumps(self.makeStatus())

            self.gateway_basic_client(stats, GATEWAY_SERVICES['ReceiveStatus'])

            self.temp += 1

            time.sleep(args)


class Light(Sensor):

    def __init__(self, ip, port, name):

        type_ = EquipmentType['SENSOR']

        queue = QUEUES['LIGHT_QUEUE']

        super().__init__(ip, port, name, type_, queue)

        self.temp = 10

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):

        message = Status()

        return message(
            StatusType['TURN_ON_OFF'], self.temp, self._id
        )

    def SendStatus(self, args):

        while True:
            stats = json.dumps(self.makeStatus())

            self.gateway_basic_client(stats, GATEWAY_SERVICES['ReceiveStatus'])

            self.temp += 1

            time.sleep(args)


class Temperature(Sensor):

    def __init__(self, ip, port, name):

        type_ = EquipmentType['SENSOR']

        queue = QUEUES['TEMPERATURE_QUEUE']

        super().__init__(ip, port, name, type_, queue)

        self.temp = 10

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):

        message = Status()

        return message(
            StatusType['TURN_ON_OFF'], self.temp, self._id
        )

    def SendStatus(self, args):

        while True:
            stats = json.dumps(self.makeStatus())

            self.gateway_basic_client(stats, GATEWAY_SERVICES['ReceiveStatus'])

            self.temp += 1

            time.sleep(args)
