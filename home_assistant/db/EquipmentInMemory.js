const fs = require("fs");
const Equipment = require("../models/Equipment");

const DB_PATH = __dirname + "/db.json";
const fileContent = (() => {
  if (fs.existsSync(DB_PATH)) {
    return fs.readFileSync(DB_PATH, "utf-8");
  } else {
    fs.writeFileSync(DB_PATH, "[]");
    return "[]";
  }
})();

class EquipmentsInMemory {
  constructor() {
    try {
      this.equipments = JSON.parse(fileContent);
    } catch (error) {
      this.equipments = [];
      console.error(error);
    }
    this.equipments = this.equipments.map(e =>
      new Equipment(e.name, e.type)
        .setIp(e.ip)
        .setPort(e.port)
        .setAllStatus(e.status)
    );
  }

  updateDb() {
    fs.writeFileSync(DB_PATH, JSON.stringify(this.equipments));
  }

  registerEquipment(newEquipment) {
    this.equipments.push(newEquipment);
    this.updateDb();
  }

  getAll() {
    return this.equipments;
  }

  getById(id) {
    return this.equipments.find(e => e.id === id);
  }

  removeById(id) {
    this.equipments = this.equipments.filter(e => e.id !== id);
    this.updateDb();
  }

  bondEquipments(id1, id2) {
    this.equipments = this.equipments.map(e => {
      if (e.id === id1) {
        let bonded = e.bondWith(id2)
        return bonded
      } else if (e.id === id2) {
        return e.bondWith(id1)
      } else {
        return e
      }
    });
    this.updateDb();
  }

  setStatus(id, type, status) {
    this.equipments = this.equipments.map(e => {
      if (e.id === id) {
        e.setStatus(type, status);
      }
      return e;
    });
    this.updateDb();
  }
}

module.exports = EquipmentsInMemory;
