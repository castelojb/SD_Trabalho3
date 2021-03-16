const PROTO_PATH = __dirname + "/../../Protobuffer/messages.proto";
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

module.exports = grpc.loadPackageDefinition(packageDefinition).EquipmentService;
