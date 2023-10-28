const fs = require('fs/promises')
const pdf = require('pdf-parse')

const getPdf = async (fileName) => {
    const count = {}
    const readFile = await fs.readFile(fileName)
    let pdfParse = await pdf(readFile)
    pdfParse = pdfParse.text.split(" ")
    const removeNewLine = pdfParse.map(s => s.trim()).filter(s => s.length > 0)
    for (let word of removeNewLine) {
        word = word.toLowerCase()
        if (count[word]) {
            count[word]++
        } else {
            count[word] = 1
        }
    }
    const orderCount = Object.entries(count)
        .sort((a, b) => b[1] - a[1])
        .reduce((obj, [key, value]) => {
            obj[key] = value;
            return obj;
        }, {});
    console.log(orderCount)
}

getPdf("../sample_file.pdf")