import string
import re


def textToDict(text,short=0):
    '''
    la punteggiatura viene eliminata
    :param text: testo come stringa
    :param short: lunghezza delle parole da eliminare quando si crea l'articolo
    :return: è un dizionario contentente come chiave la parola del testo e come valore la  sua frequenza
    '''
    # creo set per la punteggiatura
    exclude = set(string.punctuation)
    exclude.add('–')
    # elimino punteggiatura
    text = ''.join(char for char in text if char not in exclude)
    
    text = list(text.split())


    d = dict()

    for word in text:
        if len(word) <= short:
            continue
        word = word.lower()
        if word not in d:
            d[word] = 0
        d[word] += 1


    return d

#funzione per calcolare l'indice di complessità
def getIndex(d):
    out = 0.0
    for i in d:
        val = d[i]
        for j in range(val):
            out += max(0.0, min(30.0, len(i)**1.3) / ((j*0.75)+1))

    out /= 6.9
    return round(out, 1)



