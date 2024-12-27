#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
let result = 0;

if (args.length < 2) {
  result = 0;
} else {
  args.sort((a, b) => b - a);
  result = args[1];
}

console.log(result);
