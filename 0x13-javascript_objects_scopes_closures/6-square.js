#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor(size) {
    super();
    this.size = size;
    this.height = size;
    this.width = size;
  }

  charPrint(c) {
    if (c === undefined) {
      this.print;
    }
    for (let i = 0; i < this.size; i++) {
      console.log(symbol.repeat(this.size));
    }
  }
};
