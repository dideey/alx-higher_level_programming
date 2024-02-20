#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req(url + id + '/', (error, response, body) => {
  if (error) console.log(error);
  else console.log(JSON.parse(body).title);
});
