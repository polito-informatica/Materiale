"""
This program checks which words in a file are not present in a list of correctly spelled words
"""

WORDS_FILENAME = 'words.txt'
STORY_FILENAME = 'story.txt'


def main():
    words = read_words(WORDS_FILENAME)  # un insieme contente tutte le parole del dizionario
    # print(words)

    story = read_words(STORY_FILENAME)  # insieme contenente tutte le parole della storia

    # se non ci sono errori => storia è un sottoinsieme del dizionario
    # se ci sono errori => errori = storia - dizionario

    if story.issubset(words):
        print("La storia non ha errori lessicali")
    else:
        misspelled_words = story.difference(words)
        print("Le parole sbagliate sono:")
        print(sorted(misspelled_words))


def read_words(filename):
    """
    Dato il nome di un file, restituisce un **insieme** che contiene le parole uniche presenti nel file
    Attenzione: rimuove tutti i segni di punteggiatura

    :param filename: nome del file da leggere
    :return: insieme contentente tutte le parole singole
    """
    try:
        file = open(filename, 'r')
    except IOError:
        print(f"Errore nell'apertura del file {filename}")
        exit()

    insieme = set()

    for line in file:
        parole = line.rstrip().replace('-', ' ').split()
        for parola in parole:
            clean_word = only_alphabetic(parola)
            if clean_word != '':
                insieme.add(clean_word.lower())

    file.close()
    return insieme


def only_alphabetic(parola):
    """
    Rimuove tutti i caratteri INIZIALI e FINALI non alfabetici da una stringa

    :param parola: una qualsiasi parola
    :return: la stessa parola, a cui sono stati rimossi segni non alfabetici iniziali e finali
    """

    pulita = parola

    while len(pulita) > 0 and not pulita[0].isalpha():
        pulita = pulita[1:]

    while len(pulita) > 0 and not pulita[-1].isalpha():
        pulita = pulita[:-1]

    return pulita


main()
