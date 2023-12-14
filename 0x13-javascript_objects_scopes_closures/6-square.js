#!/usr/bin/node
const Square = require('./5-square');

class Square1 extends Square {
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

module.exports = Square1;
