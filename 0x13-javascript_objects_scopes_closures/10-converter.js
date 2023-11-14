#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    // Base case
    if (number < base) {
      return number.toString();
    } else {
      // Recursive case
      return convert(Math.floor(number / base)) + (number % base).toString();
    }
  };
};
