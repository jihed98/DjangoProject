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

    #print("\nDizionario da salvare: ", d)

    return d
