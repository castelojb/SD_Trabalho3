#!/usr/bin/env node

var amqp = require('amqplib/callback_api');
const equipmentsService = require("../service/inMemoryDependency");

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }
        var exchange = 'ReceiveStatus';    

        channel.assertExchange(exchange, 'fanout', {
            durable: false
        });

        channel.assertQueue('', {
            exclusive: true,
        }, function(error2, q) {
            if (error2) {
                throw error2;
            }
            console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q.queue);
            channel.bindQueue(q.queue, exchange, '');

            channel.consume(q.queue, function(msg) {
                if (msg.content) {
                    const newStatus = JSON.parse(msg.content)
                    console.log(newStatus);
                    // TODO: guardar valor no banco
                    equipmentsService.updateStatus(newStatus.id, newStatus.type, newStatus.payload) // function?
                    // TODO: disparar atuador caso necessário
                }
            }, {
                noAck: true
            });
        });
    });
});