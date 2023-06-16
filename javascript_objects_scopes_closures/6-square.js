#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c = 'X') {
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
