"""
Given a list of boolean values, use map
to convert each boolean value to its opposite
(True becomes False and False becomes True).
"""


def opposite():
    list_bool = [True, False, True, False, True, False]
    resultado = list(map(lambda x: not x, list_bool))

    print(resultado)


opposite()
