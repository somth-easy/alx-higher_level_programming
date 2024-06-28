#!/usr/bin/node

const args = process.argv.slice(2);
const len = args.length;

const arr = [];
if (len > 1) {
  for (const arg of args) {
    arr.push(parseInt(arg, 10));
  }
} else {
  console.log(0);
  process.exit();
}

arr.sort((a, b) => b - a);

console.log(arr[1]);
