const {readFile,writeFile} = require('fs/promises');

let file=[]
let fileFiltered = []
let heading = []

// memorizzara in una array di oggetti
// Rimuovi eventuali spazi bianchi iniziali o finali da ogni riga.
async function storeInDataStructure(heading,productsTxt) {
  let productTxt = []
  let products =[]
    for (let line = 0; line < productsTxt.length; line++) {
      productTxt.push(productsTxt[line].split(","))    
    }
    for (let i = 0; i < productTxt.length; i++) {
      let prodotto ={}
      for (let index = 0; index < heading.length; index++) {
        prodotto[heading[index].trim()]= productTxt[i][index].trim()
      }
      products.push(prodotto)
    }
    return products
}
// leggere il contenuto di 1 file di testo,
// Accetta il percorso come input.
async function readFiles(path) {
    try {
        const data = await readFile(path);
        const products = data.toString().trim().split("\r\n")
        heading = products.shift().split(",")
        return storeInDataStructure(heading,products)
    } catch (error) {
        console.log('errore ',error.message);
    }
}

// concatenare il contenuto di tutti i file di testo creare un unico dataset combinato
function concatenateFiles(...products) {
  products.forEach(el => {
    for (let i = 0; i < el.length; i++) {
           file.push(el[i])
        }
  });
}

// Rimuovi eventuali righe duplicate.
// Rimuovere eventuali righe con informazioni mancanti o incomplete.
function cleanDataset(allProducts) {
  for (let i = 0; i < allProducts.length; i++) {
    let datadoDoNotInsert =false
      for (let key in allProducts[i]) {
        if (allProducts[i][key].length <1) {
          datadoDoNotInsert = true;
        }
      }
      fileFiltered.forEach((item) => {
        if (allProducts[i]['Product Name']===item['Product Name']) {
          datadoDoNotInsert = true;
        }
      });
      if (!datadoDoNotInsert) {
        fileFiltered.push(allProducts[i])
      }
    }
}

// salva il set di dati pulito e concatenato in un nuovo file di testo denominato
// combined_products.txt contenente l'intestazione ogni valore separato da una virgola.
async function saveFile(file,heading) {
    try {
      let content = '';
      heading.forEach(el => {
        content+=(el.trim()+',');
      });
      file.forEach(el => {
        content+="\n"
        for (let key in el) {
          content += el[key]+','
        }
      });
      await writeFile('projects/003-concatenate-and-cleanup-multiple-files/products_files/combined_products.txt', content);
      console.log('****** eseguito con successo ******');
    } catch (err) {
      console.log(err);
    }
}

async function  callFunction() {
  let products_1 = await readFiles('projects/003-concatenate-and-cleanup-multiple-files/products_files/products_1.txt')
  let products_2 = await readFiles('projects/003-concatenate-and-cleanup-multiple-files/products_files/products_2.txt')
  let products_3 = await readFiles('projects/003-concatenate-and-cleanup-multiple-files/products_files/products_3.txt')
  concatenateFiles(products_1,products_2,products_3)
  cleanDataset(file)
  saveFile(fileFiltered,heading)
}
callFunction()