#!/usr/bin/node
const { readFile } = require('fs');

const filePath = process.argv[2];

readFile(filePath, 'utf-8', function (error, text) {
  console.log(error ? error : text);
});
