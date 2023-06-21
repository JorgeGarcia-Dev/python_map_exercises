"""
Given a list of names, use map
to convert all names to uppercase.
"""


def upper_names():
    list_name = [
        "juan",
        "pedro",
        "maria",
        "jose",
        "luis",
        "jorge",
        "carlos",
        "daniel",
        "javier",
        "julio",
    ]
    resultado = list(map(lambda x: x.upper(), list_name))

    print(resultado)


upper_names()
