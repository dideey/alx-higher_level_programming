#!/usr/bin/node
const fs = require('fs');
const rq = require('request');

rq(process.argv[2], (error, response, body) => {
  if (error) console.log('Error :', error);
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) console.log('Error:', err);
  });
});
