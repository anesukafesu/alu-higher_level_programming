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
      console.log(film.characters)
      if (film.characters.includes(characterId)) count++;
    }

    console.log(count);
  }
});
