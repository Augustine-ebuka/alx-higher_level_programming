#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 2) {
    console.log('Argument not found')
}
else if (argv.length === 3) {
    console.log('Argument found')
} else if (argv.length > 3) {
    console.log('Argument found')
}
