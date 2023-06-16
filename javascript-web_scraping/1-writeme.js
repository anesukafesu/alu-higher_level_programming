#!/usr/bin/node
const { writeFile } = require('fs');

const [filePath, text] = process.argv.slice(2, 4);

writeFile(filePath, text, "utf-8", function (error) {
    if (error) {
        console.log(error);
    }
})