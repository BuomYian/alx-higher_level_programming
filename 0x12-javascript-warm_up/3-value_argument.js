#!/usr/bin/node

// Script to print first argument passed to it

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
