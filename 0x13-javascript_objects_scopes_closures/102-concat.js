#!/usr/bin/node

const fs = require('fs').promises;

async function concatFiles (sourceFilePath1, sourceFilePath2, destinationFilePath) {
  try {
    const data1 = await fs.readFile(sourceFilePath1, 'utf8');
    const data2 = await fs.readFile(sourceFilePath2, 'utf8');
    const concatenatedContent = data1 + data2;
    await fs.writeFile(destinationFilePath, concatenatedContent, 'utf8');
  } catch (error) {
    console.error('Error:', error);
  }
}

concatFiles(process.argv[2], process.argv[3], process.argv[4]);
