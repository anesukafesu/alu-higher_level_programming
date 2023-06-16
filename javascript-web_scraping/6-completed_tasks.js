#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  else {
    const todos = JSON.parse(body);
    const usersWithCompletedTodos = {};

    for (const todo of todos) {
      if (todo.completed) {
        if (usersWithCompletedTodos[todo.userId]) {
          usersWithCompletedTodos[todo.userId]++;
        } else {
          usersWithCompletedTodos[todo.userId] = 1;
        }
      }
    }
    console.log(usersWithCompletedTodos);
  }
});
