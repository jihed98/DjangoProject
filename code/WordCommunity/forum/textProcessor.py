import string


def textToDict(text):
    # creo set per la punteggiatura ed  # elimino punteggiatura
    exclude = set(string.punctuation)
    text = ''.join(char for char in text if char not in exclude)

    text = list(text.split())

    # print("Testo trasformato in lista e tolta la punteggiatura: \n", testo)

    d = dict()

    for word in text:
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
            out += max(1, 20-j*5.3)

    out /= 6.9
    return int(round(out))


