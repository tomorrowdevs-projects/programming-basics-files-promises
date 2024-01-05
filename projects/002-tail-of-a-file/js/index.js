const { readFile } = require('fs/promises');
const readline = require('readline'); 

let path= 'projects/001-head-of-a-file/'
let showNameFile = false;
let startFrom = false;

// Accetta in ingresso il percorso del file da leggere le righe da mostrare,
// verifica che non ci siano errori nella lettura del file altrimenti emette un erroe,
// legge il file lo divide in righe le invia a showTheLines
async function readThisFile(path,numberOfLines,nameFile) { 
  try { 
    const data = await readFile(path);
    const text = data.toString() 
    let file = text.split("\n");
    if (showNameFile) {
      console.log(`====> ${nameFile} <====`);
    }
    if (numberOfLines>file.length) {
      showTheLines(file,file.length)
      console.log(`il file contiene: ${file.length} righe`)
      return
    }
    showTheLines(file,numberOfLines) 
  } catch (error) { 
    console.error(`Si è verificato un errore durante il tentativo di leggere il file: ${error.message}`); 
  } 
}

// mostra le righe del file 
function showTheLines(file, numberOfLines) {
    let lineToStart = startFrom ? numberOfLines-1 : file.length - numberOfLines;
  for (var i = lineToStart; i < file.length; i++) {
    console.log(file[i]);
  }
  console.log('');
}

// Accetta in ingresso un array, passa alla funzione showTheLines i comandi valdi 
async function validator (array) {
    let nameFiles= array.filter(item => item.includes(".txt"));
    let numberOfLines=10
    
    if (array[0] !== 'tail') {
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
            if (array[i].startsWith("+") ){
                startFrom=true
                numberOfLines=parseInt(array[i].slice(1))
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
      startFrom= false;
      validator(commands)
    }
  });
}

getUserInput();