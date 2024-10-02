const { readFile } = require('fs/promises');
let filePath = './example.txt';
let filePath2 = './example2.txt';
let filePath3 = './example3.txt';
const numberLines = 5;

readFile(filePath)
    .then((data1) => {
        console.log(data1.toString().split('\r\n').slice(0, 10).join('\r\n'));
        return data1;
    })
    .then((data2) => {
        // The -n option
        console.log(
            data2.toString().split('\r\n').slice(0, numberLines).join('\r\n')
        );
        return data2;
    })
    .then((data3) => {
        // The -v option with the name of the file
        console.log(
            `${filePath}\n ${data3
                .toString()
                .split('\r\n')
                .slice(0, numberLines - 2)
                .join('\r\n')}`
        );
    })
    .catch((error) => {
        console.log(error);
    });

// Multiple files
Promise.all([readFile(filePath), readFile(filePath2), readFile(filePath3)])
    .then(([data1, data2, data3]) => {
        console.log(data1.toString().split('\r\n').slice(0, 1).join('\r\n'));
        console.log(data2.toString().split('\r\n').slice(0, 1).join('\r\n'));
        console.log(data3.toString().split('\r\n').slice(0, 1).join('\r\n'));
    })
    .catch((error) => {
        console.log(error);
    });
