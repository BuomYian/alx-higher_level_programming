#!/usr/bin/node

// Script that print

const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
