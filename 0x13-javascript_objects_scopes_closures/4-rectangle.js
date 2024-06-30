#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  
  print (chr='X') {
    for (let x = this.height; x > 0; x--) {
      console.log(chr.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const x = this.width;
    const y = this.height;
    this.width = y;
    this.height = x;
  }
}

module.exports = Rectangle;
