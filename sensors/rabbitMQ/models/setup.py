URL_GATEWAY = 'localhost'

QUEUES = dict(
    LIGHT_QUEUE='light',

    SMOKE_QUEUE='smoke',

    TEMPERATURE_QUEUE='temperature'
)

GATEWAY_SERVICES = dict(
    Identificate='Identificate',
    ReceiveStatus='ReceiveStatus',
    EquipmentDied='EquipmentDied'
)



EquipmentType = dict(
    BOTH='BOTH',
    SENSOR='SENSOR',
    ACTUATOR='ACTUATOR'
)

StatusType = dict(
    TURN_ON_OFF='TURN_ON_OFF',
    TEMPERATURE='TEMPERATURE',
    ENV_TEMPERATURE='ENV_TEMPERATURE'
)

PORT = '5672'
