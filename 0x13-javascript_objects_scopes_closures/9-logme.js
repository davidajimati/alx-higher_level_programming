#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  count += 1;
  console.log(`${count}: ${item}`);
};
