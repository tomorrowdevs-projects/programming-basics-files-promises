const { readFile } = require('fs/promises');
const readline = require('readline'); 

let path= 'projects/001-head-of-a-file/'
let showNameFile = false;


// Accetta in ingresso il percorso del file da leggere le righe da mostrare,
// verifica che non ci siano errori nella lettura del file altrimenti emette un erroe,
// legge il file lo divide in righe le invia a showTheLines
async function readThisFile(path,numberOfLines,nameFile) { 
  try { 
    const data = await readFile(path);
    const text = data.toString() 
    let righe = text.split("\n");
    if (showNameFile) {
      console.log(`====> ${nameFile} <====`);
    }
    if (numberOfLines>righe.length) {
      showTheLines(righe,righe.length)
      console.log(`il file contiene: ${righe.length} righe`)
      return
    }
    showTheLines(righe,numberOfLines) 
  } catch (error) { 
    console.error(`Si è verificato un errore durante il tentativo di leggere il file: ${error.message}`); 
  } 
}

// mostra le righe del file 
function showTheLines(righe, numberOfLines) {
  for (var i = 0; i < numberOfLines; i++) {
    console.log(righe[i]);
  }
  console.log('');
}

// Accetta in ingresso un array, passa alla funzione showTheLines i comandi valdi 
async function validator (array) {
   
  let nameFiles= array.filter(item => item.includes(".txt"));
  let numberOfLines=10

  if (array[0] !== 'head') {
    console.log('comando non valido (exit per uscire)');
    getUserInput();
    return
  }
  for (let i = 0; i < nameFiles.length; i++) {
    let nameFile = nameFiles[i]
    for (let i = 1; i < array.length; i++) {
      if (array[i]=='-n') {
        numberOfLines= parseInt(array[i+1])
      }
      if (array[i]=='-v' ){
        showNameFile=true
      }
    }
    await readThisFile(path+nameFile,numberOfLines,nameFile)
  }
  getUserInput();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// prende l'input dall'utente trasforma in array verifica il comando 'exit' altrimenti invia linput alla funzione validetor
function getUserInput() {
  rl.question('Inserisci il comando: ', (answer) => {
    
    let commands = answer.toLowerCase().split(" ")
    
    // Verifica se l'utente ha inserito "exit" per uscire dal loop
    if (answer.toLowerCase() === 'exit') {
      rl.close(); 
    } else {
      console.log(`Hai inserito: ${answer}`);
      showNameFile = false;
      validator(commands)
    }
  });
}

getUserInput();