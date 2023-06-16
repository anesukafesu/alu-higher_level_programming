#!/usr/bin/node
const Square = require('./4-square');

class Square extends Rectangle {
  charPrint(c = 'X') {
    let line = '';

    for (let i = 0; i < this.width; i++) {
      line += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
