#!/usr/bin/node
const args = process.argv.slice(2);
const numb = args.map((arg) => parseInt(arg));
if (numb.length < 2) {
  console.log(0);
} else {
  const sortedlist = numb.sort((a, b) => b - a);
  console.log(sortedlist[1]);
}
