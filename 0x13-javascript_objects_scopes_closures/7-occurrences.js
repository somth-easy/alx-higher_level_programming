#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const arg of list) {
    if (arg === searchElement) {
      i += 1;
    }
  }
  return i;
}

