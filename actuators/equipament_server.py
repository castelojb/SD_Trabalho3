from actuator import Actuator
import grpc
from concurrent import futures
from Protobuffer import messages_pb2_grpc
import time, os
import sys
from signal import *


ip = '127.0.0.1'
external_ip = '127.0.0.1'

if __name__ == '__main__':
    print(sys.argv[1:])
    if len(sys.argv[1:]) != 3:
        raise Exception('the length of the parameters must be 3: Type Name Port')

    # get args
    type_ = sys.argv[1]
    name = sys.argv[2]
    port = int(sys.argv[3])

    if type_ == 'actuator':
        eq = Actuator(external_ip, port, name)
    else:
        raise Exception(f'Received: {type_} must be: actuator or sensor')

    # Run a gRPC server with one thread.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Adds the servicer class to the server.
    messages_pb2_grpc.add_EquipmentServiceServicer_to_server(eq, server)

    server.add_insecure_port(f'{ip}:{port}')

    server.start()

    print(f'API server started. Listening at {ip}:{port}.')
    
    def clean(*args):
        eq.EquipmentDiedClient()
        os._exit(0)

    while True:

        for sig in (SIGABRT, SIGINT, SIGTERM):
            signal(sig, clean)

        time.sleep(60)
