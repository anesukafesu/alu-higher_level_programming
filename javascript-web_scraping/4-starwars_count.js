#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  else {
    const characterId = 'https://swapi-api.alx-tools.com/api/people/18/';

    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      if (film.characters.includes(characterId)) count++;
      console.log(film.characters)
    }

    console.log(count);
  }
});
