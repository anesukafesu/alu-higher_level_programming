#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const [url, filePath] = process.argv.slice(2, 4);

request(url, function (err, res, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
