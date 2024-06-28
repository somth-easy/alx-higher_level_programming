#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] !== undefined) {
  for (const arg in args) {
    console.log(args[arg]);
  }
} else {
  console.log('No argument');
}
