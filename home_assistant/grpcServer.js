const grpc = require("@grpc/grpc-js")
const serviceApi = require("./grpc-routes/serviceApi")
const serviceImpl = require("./grpc-routes/serviceImpl")
const equipmentsService = require("./service/inMemoryDependency")
const server = new grpc.Server

server.addService(serviceApi.service, serviceImpl(equipmentsService))

module.exports = server