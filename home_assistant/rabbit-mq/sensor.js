const equipmentsService = require("../service/inMemoryDependency");

function handlingStatus(status) {
    const equipment = equipmentsService.getEquipment(status.id)
    if (equipment && equipment.subtype === "smoke") {
        if (equipment.bondedWith === undefined) {
            equipmentsService.getEquipments().then(equipments => {
                const actuators = equipments.filter(e => e.type === 'ACTUATOR')
                if (actuators.length > 0) {
                    const actuator = actuators[Math.floor(Math.random() * actuators.length)]
                    equipmentsService.bondEquipments(actuator.id, equipment.id)
                }
            })
        }
    }
    equipmentsService.updateStatus(status.id, status.type, status.payload)
}

function handleDelete(equipment) {
    equipmentsService.removeEquipment(equipment.id);
}

function listenForSensorServices(message) {
    const jsonMessage = JSON.parse(message.content)
    if (jsonMessage.service === 'ReceiveStatus') {
        handlingStatus(jsonMessage)
    } else if (jsonMessage.service === "EquipmentDied" ){
        handleDelete(jsonMessage)
    }
}

module.exports = {
    listenForSensorServices
}