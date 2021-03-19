const { getChannelForQueue } = require("./utils");
const { listenForSensorServices } = require("./sensor");

const QUEUE_NAME = "smoke"

getChannelForQueue(QUEUE_NAME)
.then(async channel => {
    return channel.consume(QUEUE_NAME, message => {
        listenForSensorServices(message)
        channel.ack(message)
    })
})