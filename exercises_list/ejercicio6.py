"""
Given a list of sentences, use map
to count the number of words in each sentence.
"""


def count_words():
    list_frases = [
        "Hola Mundo, Hola Python",
        "Python es el mejor lenguaje de Programación",
        "Mi Lenguaje favorito es Python",
        "Amo programar en Python",
        "Python Lover",
    ]
    resultado = list(map(lambda x: len(x.split()), list_frases))

    print(resultado)


count_words()
