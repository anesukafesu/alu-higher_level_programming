#!/usr/bin/node

const { request } = require('http');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  else console.log(res.statusCode);
});
