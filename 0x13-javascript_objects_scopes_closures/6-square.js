#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    const symbol = c || 'X';
    const { height, width } = this;

    for (let i = 0; i < height; i++) {
      console.log(symbol.repeat(width));
    }
  }
};
