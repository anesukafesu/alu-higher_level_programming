#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let numberOfTimes = 0;

  for (const element of list) {
    if (element === searchElement) {
      numberOfTimes += 1;
    }
  }

  return numberOfTimes;
}

module.exports = { nbOccurences };
