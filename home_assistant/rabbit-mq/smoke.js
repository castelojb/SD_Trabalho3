const { getChannelForQueue } = require("./utils");
const equipmentsService = require("../service/inMemoryDependency");

const QUEUE_NAME = "smoke"

function handlingStatus(status) {
    console.log(status)
    equipmentsService.updateStatus(status.id, status.type, status.payload)
}

getChannelForQueue(QUEUE_NAME)
.then(channel => {
    return channel.consume(QUEUE_NAME, message => {
        const jsonMessage = JSON.parse(message.content)
        if (jsonMessage.service === 'ReceiveStatus') {
            handlingStatus(jsonMessage)
        }

        channel.ack(message)
    })
})