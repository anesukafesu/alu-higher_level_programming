#!/usr/bin/node

function esrever (list) {
  let reversedList = [];
  // Looping through the list from the back
  for (let i = list.length - 1; i >= 0; i++) {
    reversedList.push(list[i]);
  }
  return reversedList;
}

module.exports = { esrever };
