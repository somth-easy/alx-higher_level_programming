#!/usr/bin/node

const args = process.argv.slice(2);

if (/^-?\d+$/.test(args[0])) {
  const myInt = parseInt(args[0], 10);
  if (myInt > 0) {
    for (let i = myInt; i > 0; i--) {
      console.log('C is fun');
    }
  }
} else if (args.length === 0) {
  console.log('Missing number of occurences');
}
