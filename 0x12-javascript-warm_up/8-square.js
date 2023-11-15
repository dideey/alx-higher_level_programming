#!/usr/bin/node
const arg = process.argv.slice(2);
const size = parseInt(arg[0]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let sq = '';
    for (let j = 0; j < size; j++) {
      sq += 'X';
    }
    console.log(sq);
  }
}
