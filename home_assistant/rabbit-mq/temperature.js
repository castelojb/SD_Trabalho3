const { getChannelForQueue } = require("./utils");
const { listenForSensorServices } = require("./sensor");

const QUEUE_NAME = "temperature"

getChannelForQueue(QUEUE_NAME)
.then(channel => {
    return channel.consume(QUEUE_NAME, message => {
        listenForSensorServices(message)

        channel.ack(message)
    })
})