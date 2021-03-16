#!/usr/bin/env node

var amqp = require("amqplib/callback_api");
const Equipment = require("../models/Equipment");
const equipmentsService = require("../service/inMemoryDependency");

amqp.connect("amqp://localhost", function (error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function (error1, channel) {
    if (error1) {
      throw error1;
    }
    //var queue = "smoke";
    var exchange = "dsdsdlçkml";

    channel.assertExchange(exchange, "fanout", {
      durable: false,
    });

    channel.assertQueue(
      'identificate',
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
          const Identificate = JSON.parse(msg.content)
          console.log(Identificate);
          const newEquipment = new Equipment(Identificate.name, Identificate.type)
            .setIp(Identificate.ip)
            .setPort(Identificate.port)
            .setType(Identificate.type);
          equipmentsService.registerEquipment(newEquipment);
          let EquipmentId = {
            value: newEquipment.id,
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
