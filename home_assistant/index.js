if (process.env.NODE_ENV !== "production") require("dotenv").config()

const grpc = require("@grpc/grpc-js")
const httpPort = process.env.HTTP_PORT || 3000
const httpHost = process.env.HTTP_HOST || "127.0.0.1"

const httpServer = require("./httpServer")
httpServer.listen(httpPort, httpHost, () => {
    console.log(`> HTTP Server running on address ${httpHost}:${httpPort}`)
})

const grpcPort = process.env.GRPC_PORT || 3001
const grpcHost = process.env.GRPC_HOST || "127.0.0.1"
const address = `${grpcHost}:${grpcPort}`

const insecureCredential = grpc.ServerCredentials.createInsecure()
const grpcServer = require("./grpcServer")
grpcServer.bindAsync(address, insecureCredential, error => {
    if (error) {
        return console.error(error)
    }
    grpcServer.start()
    console.log(`> GRPC Server running on address ${grpcHost}:${grpcPort}`)
})

require('./rabbit-mq')