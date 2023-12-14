#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    let toPrint = '';
    let char = 'X';
    if (c) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        toPrint += char;
      }
      if (i < this.height - 1) {
        toPrint += '\n';
      }
    }
    console.log(toPrint);
  }
}

module.exports = Square;
