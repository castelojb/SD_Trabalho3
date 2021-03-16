from models.sensors_core import Smoke, Light, Temperature

import time, os
import sys
from signal import *

ip = '0.0.0.0'

external_ip = '0.0.0.0'

if __name__ == '__main__':

    if len(sys.argv[1:]) != 3:
        raise Exception('the length of the parameters must be : Type Name Port')

    # get args
    type_ = sys.argv[1]
    name = sys.argv[2]
    port = int(sys.argv[3])

    if type_ == 'smoke':
        eq = Smoke(external_ip, port, name)
    elif type_ == 'light':
        eq = Light(external_ip, port, name)
    elif type_ == 'temperature':
        eq = Temperature(external_ip, port, name)
    else:
        raise Exception(f'Received: {type_} must be: smoke, light or temperature')

    print(f'Sensor {type_} is up and fine.')


    def clean(*args):
        eq.EquipmentDiedClient()
        os._exit(0)


    while True:

        for sig in (SIGABRT, SIGINT, SIGTERM):
            signal(sig, clean)

        time.sleep(60)
