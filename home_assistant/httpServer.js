const express = require("express")
require('express-async-errors')
const app = express()
const http = require("http")
const server = http.createServer(app)
const bodyParser = require("body-parser")
const equipmentsService = require("./service/inMemoryDependency")
const cors = require("cors")
const equipmentsRouter = require("./http-routes/equipments")

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.use(cors({
    origin: "*"
}))

app.use("/api/equipments", equipmentsRouter(equipmentsService))
app.use((err, req, res, next) => {
    res.status(500).json({
        message: err.message
    });
})


module.exports = server