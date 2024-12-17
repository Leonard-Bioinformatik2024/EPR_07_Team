"""This module contains the class Produkt.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


class Produkt:
    def __init__(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)):
            raise ValueError("Ungültige Eingabe: Name muss ein String und Price eine Zahl sein.")

        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")

        self.name = name
        self.price = price

    def __str__(self):
        return f"Produkt: {self.name}, Preis: {self.price} EUR"
