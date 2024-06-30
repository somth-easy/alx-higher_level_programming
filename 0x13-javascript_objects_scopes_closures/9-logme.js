#!/usr/bin/node
let cnt = 0;
function logMe (item) {
  console.log(`${cnt}: ${item}`);
  cnt += 1;
}

module.exports = logMe;
