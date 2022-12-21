#!/usr/bin/node

// Script to print the number of arguments

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument fount' : 'Arguments found');
