class Equipment {
  constructor(name, type) {
    this.name = name;
    this.type = type;
    this.subtype = undefined;
    this.id = Math.random().toString(16).substring(2);
    this.status = {};
    this.ip = "0.0.0.0";
    this.port = 3000;
    this.bondedWith = undefined
  }

  setType(type) {
    this.type = type;
    return this;
  }

  setSubtype(subtype) {
    this.subtype = subtype;
    return this;
  }

  bondWith(id) {
    this.bondedWith = id;
    return this;
  }

  setAllStatus(status) {
    this.status = status;
    return this;
  }

  setStatus(type, status) {
    this.status = {
      ...this.status,
      [type]: status,
    };
    return this;
  }

  setIp(ip) {
    this.ip = ip;
    return this;
  }

  setPort(port) {
    this.port = port;
    return this;
  }
}

module.exports = Equipment;
