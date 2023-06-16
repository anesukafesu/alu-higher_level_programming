#!/usr/bin/node

function nbOccurrences(list, searchElement) {
  let numberOfTimes = 0;

  for (let element of list) {
    if (element === searchElement) {
      numberOfTimes += 1;
    }
  }

  return numberOfTimes;
}

module.exports = { nbOccurrences };
