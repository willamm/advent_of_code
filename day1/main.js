const fs = require('fs');
const readline = require('readline')

const createElf = () => {
    let rl = readline.createInterface({
        input: fs.createReadStream("./input"),
        output: process.stdout,
        terminal: false
    });
    let elves = []
    let current = 0;
    let max = 0;
    rl.on('line', text => {
        if (text !== "\n") {
            current = current + parseInt(text);
            console.log(current);
        } else {
            max = Math.max(current, max);
        }
    })
}
createElf();
