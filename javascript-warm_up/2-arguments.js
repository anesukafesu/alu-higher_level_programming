#!/usr/bin/node
let numberOfArgs = process.argv.length - 2;

if (numberOfArgs == 0) {
  console.log('No arguments');
} else if (numberOfArgs == 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found')
}
