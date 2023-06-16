#!/usr/bin/node

function converter (base) {
  return function (number) {
    return Number(number.toString(base));
  };
}

module.exports = { converter };
