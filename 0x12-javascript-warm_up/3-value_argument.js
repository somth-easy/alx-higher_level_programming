#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] !== undefined) {
    console.log(args.join(' '));
} else {
  console.log('No argument');
}
