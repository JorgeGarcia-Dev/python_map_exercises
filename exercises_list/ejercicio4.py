"""
Given a list of lists, use map
to get the sum of each inner list.
"""


def sum_list():
    list_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    resultado = list(map(lambda x: sum(x), list_list))

    print(resultado)


sum_list()
