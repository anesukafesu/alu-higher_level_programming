#!/usr/bin/node

let firstArg = '';

try {
  firstArg = process.argv[2];
} catch (e) {
  // Do nothing 🙂
}

console.log(firstArg || 
  
