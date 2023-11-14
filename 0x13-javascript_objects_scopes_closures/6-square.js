#!/usr/bin/node

const Squares = require('./5-square.js');
class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let display = '';
      for (let j = 0; j < this.width; j++) {
        display += c;
      }
      console.log(display);
    }
  }
}
module.exports = Square;
