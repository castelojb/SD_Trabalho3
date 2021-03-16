const { getChannelForQueue } = require("./utils");
const equipmentsService = require("../service/inMemoryDependency");
const { listenForSensorServices } = require("./sensor");

const QUEUE_NAME = "smoke"

getChannelForQueue(QUEUE_NAME)
.then(channel => {
    return channel.consume(QUEUE_NAME, message => {
        listenForSensorServices(message)
        channel.ack(message)
    })
})