#!/usr/bin/node
const argv = require('process');
if (argv[2] === undefined) {
    console.log('not found');
} else {
    console.log(argv[2]);
}