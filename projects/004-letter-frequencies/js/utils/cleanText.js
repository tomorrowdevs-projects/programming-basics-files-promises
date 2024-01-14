// Pulische il testo immesso rimuovendo segni di punteggiatura, numeri e altri caratteri diversi dalle lettere.
function cleanText(txt) {
    const toDelete = /\$|,|@|#|~|`|\%|\*|\^|\&|\(|\)|\+|\=|\[|\-|\_|\]|\[|\}|\{|\;|\:|\'|\"|\<|\>|\?|\||\\|\!|\$|\.|\ |[0-9]?/g;

    return txt.replace(toDelete, "").toLowerCase();
}

module.exports = {cleanText}