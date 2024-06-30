#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const chr = 'X';
    for (let x = this.height; x > 0; x--) {
      console.log(chr.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
