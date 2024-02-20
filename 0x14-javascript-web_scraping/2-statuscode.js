#!/usr/bin/node
const rq = require('request');
rq(process.argv[2], (error, response) => {
        if (error) {
            console.error('Error:', error);
        } else {
            console.log('Code:', response.statusCode);
        }
    });