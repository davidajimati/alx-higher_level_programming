#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    const symbol = c || 'X';
    const { size } = this;

    for (let i = 0; i < size; i++) {
      console.log(symbol.repeat(size));
    }
  }
};
