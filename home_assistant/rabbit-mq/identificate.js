const Equipment = require("../models/Equipment");
const equipmentsService = require("../service/inMemoryDependency");
const { getChannelForQueue } = require("./utils");

const QUEUE_NAME = "identificate"

function handleMessaging({ channel, content: identificate, properties: { replyTo, correlationId } }) {
    let equipment = new Equipment(identificate.name, identificate.type)
        .setIp(identificate.ip)
        .setPort(identificate.port)
    
    if (equipment.type === "SENSOR") equipment = equipment.setSubtype(identificate.sensor_type)
    equipmentsService.registerEquipment(equipment)
    console.log(identificate)
    const EquipmentId = { value: equipment.id }
    channel.sendToQueue(replyTo, Buffer.from(JSON.stringify(EquipmentId)), {
        correlationId
    })
}

getChannelForQueue(QUEUE_NAME)
.then(channel => {
    return channel.consume(QUEUE_NAME, message => {
        console.log(message)
        handleMessaging({
            channel,
            content: JSON.parse(message.content),
            properties: message.properties
        })
        channel.ack(message)
    })
})
.catch(console.error)