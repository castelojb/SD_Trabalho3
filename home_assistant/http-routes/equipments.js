const { Router } = require("express");
const Equipment = require("../models/Equipment");
const { body, validationResult } = require("express-validator");


const equipmentsRouter = new Router()

const updateStatusValidations = [
    body('type').isString(),
    body('status').isNumeric(),
]

module.exports = equipmentsService => {
    equipmentsRouter
    .get("/", async (req, res) => {
        let type = req.query.type
        if (type) {
            res.json(await equipmentsService.getEquipmentsOfType(type))
        } else {
            res.json(await equipmentsService.getEquipments())
        }
    })
    .post("/", (req, res) => {
        const newEquipment = Object.assign(new Equipment, req.body)
        equipmentsService.registerEquipment(newEquipment)
        res.status(201).json(equipmentsService.getEquipment(newEquipment.id))
    })
    .get("/:equipmentId/status", (req, res) => {
        const type = req.query.type
        equipmentsService.getEquipmentStatus(req.params.equipmentId, type)
        .then(status => res.status(200).json(status))
        .catch(error => res.status(500).json(error))
    })
    .put("/:equipmentId", ...updateStatusValidations, (req, res) => {
        const errors = validationResult(req);
        const { type, status } = req.body
        const { equipmentId } = req.params
        if (errors.isEmpty()) {
            equipmentsService.updateStatus(equipmentId, type, status)
            res.status(200).json(equipmentsService.getEquipment(equipmentId))
        } else {
            res.status(400).json({
                errors: errors.array()
            })
        }
    })

    return equipmentsRouter
}