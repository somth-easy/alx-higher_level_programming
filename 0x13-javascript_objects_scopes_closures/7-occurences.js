#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let i = 0;
  for (const arg of list) {
    if (arg === searchElement) {
      i++;
    }
  }
  return i;
}

module.exports = nbOccurences;
