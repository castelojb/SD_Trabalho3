#!/usr/bin/env node

var amqp = require("amqplib/callback_api");

amqp.connect("amqp://localhost", function (error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function (error1, channel) {
    if (error1) {
      throw error1;
    }
    //var queue = "smoke";
    var exchange = "Identificate";

    channel.assertExchange(exchange, "fanout", {
      durable: false,
    });

    channel.assertQueue(
      '',
      {
        exclusive: true,
      },
      function (error2, q) {
        if (error2) {
          throw error2;
        }
        channel.bindQueue(q.queue, exchange, "");

        channel.prefetch(1);
        console.log(" [x] Awaiting RPC requests");

        channel.consume(q.queue, function reply(msg) {
          console.log(JSON.parse(msg.content));
          
          // TODO: criar Equipamento e pegar id de verdade
          let EquipmentId = {
            value: 2,
          };

          channel.sendToQueue(
            msg.properties.replyTo,
            Buffer.from(JSON.stringify(EquipmentId)),
            {
              correlationId: msg.properties.correlationId,
            }
          );

          channel.ack(msg);
        });
      }
    );
  });
});
