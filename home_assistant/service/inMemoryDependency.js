const EquipmentService = require("./EquipmentsService");
const EquipmentsInMemory = require("../repository/EquipmentInMemory");

const equipmentsRepository = new EquipmentsInMemory();
const equipmentsService = new EquipmentService(equipmentsRepository);

module.exports = equipmentsService;
