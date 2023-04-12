#!/usr/bin/node
exports.converter = function (base) {
  return subject => subject.toString(base);
};
