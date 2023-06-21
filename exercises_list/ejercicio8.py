"""
Given a list of numbers, use map to round
each number to the nearest integer.
"""


def round_out():
    lista = [1.2, 2.5, 3.7, 4.6, 5.9, 6.1, 7.4, 8.2, 9.9, 10.5]
    resultado = list(map(lambda x: round(x), lista))

    print(resultado)


round_out()
