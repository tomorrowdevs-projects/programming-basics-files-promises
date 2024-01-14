// Definire le funzioni
// leggere il file, **
// elaborazione del testo,
// analisi della frequenza delle lettere,
// visualizzazione,
// principale

const readline = require('readline'); 
const {readThisFile} = require("./utils/readFile")
const {cleanText} = require("./utils/cleanText")
const {countCharacters} = require("./utils/countCharacters")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// prende l'input dall'utente, verifica il comando 'exit', verifica il percorso di un file di testo,
// verifica stato inserito un testo
function getUserInput() {
  rl.question('Inserisci il testo oppure il percorso del file .txt da contare, exit per uscire: ', async (answer) => {
    let txt = answer.toLowerCase().trim()
    if (txt === 'exit') {
      console.log(txt);
      rl.close(); 
      return
    }
    if (txt.endsWith(".txt")) {
      txt = await readThisFile(txt)
    }
    txt = await cleanText(txt)
    countCharacters(txt)
    getUserInput()
  });
}
getUserInput()