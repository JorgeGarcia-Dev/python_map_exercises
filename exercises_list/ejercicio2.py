"""
Given a list of words, use map
to get the length of each word.
"""


def lenght_words():
    list_words = ["Estoy", "Programando", "En", "Python", "Hoy", "!!"]
    resultado = list(map(lambda x: len(x), list_words))

    print(resultado)


lenght_words()
