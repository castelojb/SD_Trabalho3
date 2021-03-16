const Equipment = require("../models/Equipment");
const EquipmentClient = require("./equipmentClient");
const grpc = require("@grpc/grpc-js");

module.exports = service => ({
  Identificate(call, callback) {
    const info = call.request;
    const newEquipment = new Equipment(info.name, info.type)
      .setIp(info.ip)
      .setPort(info.port)
      .setType(info.type);
    service.registerEquipment(newEquipment);

    callback(null, {
      value: newEquipment.id,
    });
  },
  ReceiveStatus(call, callback) {
    const status = call.request;
    if (service.getEquipment(status.id)) {
      service.updateStatus(status.id, status.type, status.payload);
      callback(null, status);
    } else {
      callback({
        message: "Equipamento não encontrado.",
        status: grpc.status.NOT_FOUND,
      });
    }
  },
  EquipmentDied(call, callback) {
    const { value: id } = call.request;
    if (service.getEquipment(id)) {
      service.removeEquipment(id);
      callback(null, {});
    } else {
      callback(null, {});
    }
  },
});
