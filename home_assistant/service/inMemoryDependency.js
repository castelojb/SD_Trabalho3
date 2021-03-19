const EquipmentService = require("./EquipmentsService");
const EquipmentsInMemory = require("../db/EquipmentInMemory");

const equipmentsRepository = new EquipmentsInMemory();
const equipmentsService = new EquipmentService(equipmentsRepository);

module.exports = equipmentsService;
