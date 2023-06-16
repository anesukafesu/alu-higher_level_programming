#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  else {
    const targetId = '18';

    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      for (const character of film.characters) {
        // Getting the id from the character url as a string
        const characterId = String(character.split('/').slice(-2, -1)[0]);
        if (targetId === characterId) count++;
      }
    }

    console.log(count);
  }
});
