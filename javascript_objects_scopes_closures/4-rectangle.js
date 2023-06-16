#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let line = '';

    for (let i = 0; i < this.width; i++) {
      line += 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate() {
    let tempHeight = this.height;
    this.height = this.width;
    this.width = tempHeight;
  }

  double() {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
