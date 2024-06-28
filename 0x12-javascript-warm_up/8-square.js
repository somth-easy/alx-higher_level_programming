#!/usr/bin/node

const args = process.argv.slice(2);
const myChr = 'X';

if (/^-?\d+$/.test(args[0])) {
  const myInt = parseInt(args[0], 10);
  if (myInt > 0) {
    for (let i = myInt; i > 0; i--) {
      console.log(myChr.repeat(myInt));
    }
  } else if (myInt < 0) {
    process.exit();
  }
} else if (!/^-?\d+$/.test(args[0]) && args.length < 1) {
  console.log('Missing size');
}
