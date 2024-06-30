#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    if (c !== undefined) {
      this.print(c);
    } else {
      this.print();
    }
  }
}

module.exports = Square;
