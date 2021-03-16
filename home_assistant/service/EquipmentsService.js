const EquipmentClient = require("../grpc-routes/equipmentClient");
const grpc = require("@grpc/grpc-js");

class EquipmentService {
  constructor(repository) {
    this.repository = repository;
  }

  // populateStatus(equipment) {
  //     const client = new EquipmentClient(
  //         `${equipment.ip}:${equipment.port}`,
  //         grpc.credentials.createInsecure()
  //     )
  //     return new Promise((resolve, reject) => {
  //         Promise.all(['VALUE', 'TURN_ON_OFF'].map(type =>
  //             new Promise((resolve, reject) =>
  //                 client.GetStatus({ type }, (error, response) => {
  //                     if (error) reject(error)
  //                     resolve(response)
  //                 })
  //             )
  //         )).then(([temperatureStatus, tunnedOnStatus]) => {
  //             resolve(
  //                 equipment
  //                 .setStatus(temperatureStatus.type, temperatureStatus.payload)
  //                 .setStatus(tunnedOnStatus.type, tunnedOnStatus.payload)
  //             )
  //         }).catch(reject)
  //     })
  // }

  getEquipments() {
    return Promise.resolve(this.repository.getAll());
  }

  getEquipment(id) {
    return this.repository.getById(id);
  }

  removeEquipment(id) {
    return this.repository.removeById(id);
  }

  getEquipmentStatus(id, type) {
    const equipment = this.repository.getById(id);
    const client = new EquipmentClient(
      `${equipment.ip}:${equipment.port}`,
      grpc.credentials.createInsecure()
    );
    return new Promise((resolve, reject) => {
      client.GetStatus({ type }, (error, response) => {
        if (error) return reject(error);
        resolve(response);
      });
    });
  }

  async getEquipmentsOfType(type) {
    return (await this.repository.getAll()).filter(e => e.type === type);
  }

  registerEquipment(newEquipment) {
    this.repository.registerEquipment(newEquipment);
  }

  updateStatus(id, type, status) {
    const equipment = this.repository.getById(id);
    this.repository.setStatus(id, type, status);
    const address = `${equipment.ip}:${equipment.port}`
    const client = new EquipmentClient(address, grpc.credentials.createInsecure())
    if (client.type === "actuator") {
      client.ReceiveUpdate({
        type,
        payload: status
      }, (error, response) => {
          if (error) throw error;
      })
    }
  }
}

module.exports = EquipmentService;
