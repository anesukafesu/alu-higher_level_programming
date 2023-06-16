#!/usr/bin/node

const {request} = require("http");

const url = process.argv[2];

request(url, function(res) {
    console.log(res.statusCode)
})