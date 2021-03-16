function handlingStatus(status) {
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