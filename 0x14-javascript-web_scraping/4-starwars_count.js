#!/usr/bin/node
const req = require('request');
const url = process.argv[2]

req(url, (error, response, body)=> {
    if (error) console.log(error);
    else {
        const response = JSON.parse(body).results;
        let count = 0;
        response.results.foreach(title => {
            title.character.foreach(url => {
                const id = parseInt(url.split('/').slice(-2, -1)[0]);
                if (id == 18) {
                    count++;
                }
            })
        })
      
        console.log(count);
    }
});
