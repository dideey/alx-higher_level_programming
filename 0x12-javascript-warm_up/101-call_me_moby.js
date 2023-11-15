#!/usr/bin/node
exports.moby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
