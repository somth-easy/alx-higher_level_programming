#!/usr/bin/node

function factorial (x) {
  if (x === 0) {
    return 1;
  }

  return x * factorial(x - 1);
}

const args = process.argv.slice(2);
const argLen = args.length;

if (argLen === 0) {
  console.log(1);
} else {
  if (parseInt(args[0])) {
    console.log(factorial(parseInt(args[0])));
  } else {
    console.log(1);
  }
}
