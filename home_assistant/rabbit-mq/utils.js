const open = require("amqplib").connect("amqp://localhost");

function getChannelForQueue(queue) {
    return new Promise((resolve, reject) => {
        open
        .then(connection => connection.createChannel())
        .then(channel => {
            channel.prefetch(1);
            return channel.assertQueue(queue, { durable: false }).then(() => resolve(channel))
        })
        .catch(reject)
    })
}

module.exports = {
    getChannelForQueue
}