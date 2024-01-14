// const {getUserInput} = require("../index")
const charactersToCount = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","è","é","ù","ò","à"];

//calcolere la frequenza di ciascuna lettera (senza distinzione tra maiuscole e minuscole),
// Visualizza i dati sulla frequenza delle lettere utilizzando un grafico a barre,
// Richiama la funzione getUserInput per analizzare un altro testo o uscire dal programma.
function countCharacters(text) {
    charactersToCount.forEach(el => {
        let count = 0
        for (let i = 0; i < text.length; i++) {
            text[i]===el;
            count += text[i]===el ? 1 : 0;
        }
        if (count>0) {
            let quadratovuoto ='\u2591'
            let quadratoPieno ='\u2588'
            console.log(el,quadratoPieno.repeat(count));
        }
    });
    // getUserInput()
}
module.exports = {countCharacters}