#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    if (c !== undefined) {
      this.chr = c;
    }
    this.print();
  }
}

module.exports = Square;
