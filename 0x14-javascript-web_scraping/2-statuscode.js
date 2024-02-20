#!/usr/bin/node
const rq = require('request');
rq.get(process.argv[2], (error, response) => {
  if (error) {
    console.error('Error :');
  } else {
    const statusCode = response.statusCode;
    console.log('Code :', statusCode);
  }
});
