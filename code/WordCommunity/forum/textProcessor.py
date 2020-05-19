import string


def textToDict(text,short=0):
    # creo set per la punteggiatura ed  # elimino punteggiatura
    exclude = set(string.punctuation)
    text = ''.join(char for char in text if char not in exclude)
    
    text = list(text.split())

    # print("Testo trasformato in lista e tolta la punteggiatura: \n", descrizione)

    d = dict()

    for word in text:
        if len(word) <= short:
            continue
        word = word.lower()
        if word not in d:
            d[word] = 0
        d[word] += 1

    # print("\nDizionario da salvare: ", d)

    return d


def getIndex(d):
    out = 0.0
    for i in d:
        val = d[i]
        for j in range(val):
            out += max(0.0, min(30.0, len(i)**1.3) / ((j*0.75)+1))

    out /= 6.9
    return round(out, 1)

# def getIndex(d):
#    out = 0.0
#    for i in d:
#        val = d[i]
#        for j in range(val):
#            out += max(1, 20-j*5.3)
#
#    out /= 6.9
#   return int(round(out))

