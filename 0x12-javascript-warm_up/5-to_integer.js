#!/usr/bin/node

const args = process.argv.slice(2);

if (/^-?\d+(\.\d+)?$/.test(args[0])) {
  console.log(`My number: ${parseInt(args[0], 10)}`);
} else {
  console.log('Not a number');
}
