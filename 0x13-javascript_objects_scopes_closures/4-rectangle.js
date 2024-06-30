#!/usr/bin/node
class Rectangle {
  const chr = 'X';
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = this.height; x > 0; x--) {
      console.log(chr.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
    }
  }

  rotate () {
    this.width = h;
    this.height = w;
  }
}

module.exports = Rectangle;
