#!/usr/bin/node
const { request } = require('http');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/:${id}`;

request(url, (res) => {
    console.log(JSON.parse(res.body).title);
})