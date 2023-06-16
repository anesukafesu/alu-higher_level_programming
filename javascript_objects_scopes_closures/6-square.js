#!/usr/bin/node
const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c = "X") {
    let line = "";

    for (let i = 0; i < this.width; i++) {
      line += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
