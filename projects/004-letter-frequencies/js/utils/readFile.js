const { readFile } = require('fs/promises');

// Accetta in ingresso il percorso del file da leggere,
// verifica che non ci siano errori nella lettura del file altrimenti emette un erroe,
// ritorna una stringa di testo
async function readThisFile(path) { 
    try { 
      const data = await readFile(path);
      const text = data.toString() 
      return text 
    } catch (error) { 
      console.error(`Si è verificato un errore durante il tentativo di leggere il file: ${error.message}`); 
    } 
}

module.exports = {readThisFile}