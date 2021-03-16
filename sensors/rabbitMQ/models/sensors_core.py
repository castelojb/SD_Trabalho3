import json
import time
from threading import Thread

from models.gateway_clients import GatewayRpcClient, GatewayBasicClient
from models.messages import *
from models.setup import StatusType, EquipmentType, QUEUES, GATEWAY_SERVICES

import random

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
            self._id,
            GATEWAY_SERVICES['EquipmentDied']
        ))

        self.gateway_basic_client(request)

        self.gateway_basic_client.kill()

    def makeIdentification(self):
        message = Identification()
        return message(
            self.name, self.type, self.ip, self.port, GATEWAY_SERVICES['Identificate']
        )

    def IdentificateClient(self):

        request = json.dumps(self.makeIdentification())
        print(request)
        response = json.loads(self.gateway_rpc_client(request))

        self.gateway_rpc_client.kill()

        self._id = response['value']


class Smoke(Sensor):

    def __init__(self, ip, port, name):

        type_ = EquipmentType['SENSOR']

        queue = QUEUES['SMOKE_QUEUE']

        super().__init__(ip, port, name, type_, queue)

        self.smoke = False

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):

        message = Status()

        return message(
            StatusType['HAVE_SMOKE'], self.smoke, self._id, GATEWAY_SERVICES['ReceiveStatus']
        )

    def SendStatus(self, args):

        while True:
            stats = json.dumps(self.makeStatus())

            self.gateway_basic_client(stats)

            self.smoke = not self.smoke

            time.sleep(args)


class Light(Sensor):

    def __init__(self, ip, port, name):

        type_ = EquipmentType['SENSOR']

        queue = QUEUES['LIGHT_QUEUE']

        super().__init__(ip, port, name, type_, queue)

        self.light = random.randint(0, 100)

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):

        message = Status()

        return message(
            StatusType['LIGHT_VALUE'], self.light, self._id, GATEWAY_SERVICES['ReceiveStatus']
        )

    def SendStatus(self, args):

        while True:
            stats = json.dumps(self.makeStatus())

            self.gateway_basic_client(stats)

            self.light = random.randint(0, 100)

            time.sleep(args)


class Temperature(Sensor):

    def __init__(self, ip, port, name):

        type_ = EquipmentType['SENSOR']

        queue = QUEUES['TEMPERATURE_QUEUE']

        super().__init__(ip, port, name, type_, queue)

        self.temp = random.randint(25, 50)

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):

        message = Status()

        return message(
            StatusType['TEMPERATURE'], self.temp, self._id, GATEWAY_SERVICES['ReceiveStatus']
        )

    def SendStatus(self, args):

        while True:
            stats = json.dumps(self.makeStatus())

            self.gateway_basic_client(stats)

            self.temp = random.randint(25, 50)

            time.sleep(args)
