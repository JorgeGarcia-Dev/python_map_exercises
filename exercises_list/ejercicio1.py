"""
Given a list of numbers, use map
to calculate the square of each number.
"""


def squared_num():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = list(map(lambda x: x**2, lista))

    print(resultado)


squared_num()
