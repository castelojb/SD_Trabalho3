const { getChannelForQueue } = require("./utils");
const equipmentsService = require("../service/inMemoryDependency");

const QUEUE_NAME = "temperature"

function handleStatus(status) {
    equipmentsService.updateStatus(status.id, status.type, status.payload)
}

function handleDelete(equipment) {
  equipmentsService.removeEquipment(equipment.id);
}

getChannelForQueue(QUEUE_NAME)
.then(channel => {
    return channel.consume(QUEUE_NAME, message => {
        const jsonMessage = JSON.parse(message.content)
        if (jsonMessage.service === 'ReceiveStatus') {
            handleStatus(jsonMessage)
        } else if (jsonMessage.service === "EquipmentDied" ){
            handleDelete(jsonMessage)
        }

        channel.ack(message)
    })
})