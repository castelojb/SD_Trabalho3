URL_GATEWAY = 'amqp://localhost'

QUEUES = dict(
    LIGHT_QUEUE='light',

    SMOKE_QUEUE='smoke',

    TEMPERATURE_QUEUE='temperature'
)

GATEWAY_SERVICES = dict(
    Identificate='identificate',
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
    ENV_TEMPERATURE='ENV_TEMPERATURE',
    HAVE_SMOKE='HAVE_SMOKE',
    LIGHT_VALUE='LIGHT_VALUE'
)

PORT = '5672'
