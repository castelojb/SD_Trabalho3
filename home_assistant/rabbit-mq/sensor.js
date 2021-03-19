const equipmentsService = require("../service/inMemoryDependency");

function handlingStatus(status) {
    const equipment = equipmentsService.getEquipment(status.id)
    if (equipment && equipment.bondedWith === undefined) {
        equipmentsService.getEquipments().then(equipments => {
            const actuators = equipments.filter(e => e.type === 'ACTUATOR')

            if (equipment.subtype === "smoke") {
                let sprinklers = actuators.filter(e => e.subtype === "Sprinkler")
                if (sprinklers.length > 0) {
                    const sprinkler = sprinklers[Math.floor(Math.random() * sprinklers.length)]
                    equipmentsService.bondEquipments(sprinkler.id, equipment.id)
                }
            } else if (equipment.subtype === "light") {
                let lamps = actuators.filter(e => e.subtype === "Lampada")
                if (lamps.length > 0) {
                    const lamp = lamps[Math.floor(Math.random() * lamps.length)]
                    equipmentsService.bondEquipments(lamp.id, equipment.id)
                }
            } else if (equipment.subtype === "temperature") {
                let airs = actuators.filter(e => e.subtype === "Ar")
                if (airs.length > 0) {
                    const air = airs[Math.floor(Math.random() * airs.length)]
                    equipmentsService.bondEquipments(air.id, equipment.id)
                }
            }
        })
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