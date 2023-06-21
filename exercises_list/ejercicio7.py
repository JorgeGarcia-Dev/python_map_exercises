"""
Given a list of strings, use map to get
a list of the strings in reverse order.
"""


def reverse_list():
    list_words = ["ana", "oso", "kayak", "zaz", "salas", "somos"]
    resultado = list(map(lambda x: x[::-1], list_words))

    print(resultado)


reverse_list()
