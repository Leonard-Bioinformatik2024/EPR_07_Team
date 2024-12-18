"""This module contains the class Product.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


class Product:
    """Contains a __str__() method to create a string 
    containing the name and price of the product.
    """

    def __init__(self, name, price):

        # checking if the name and price are of the correct type
        # otherwise it will cause errors later down the line
        if not isinstance(name, str) or not isinstance(price, (int, float)):
            raise ValueError("invalide input: name must be a string and price a number!")

        self.name = name
        self.price = price

    def __str__(self):
        """source: https://www.pythontutorial.net/python-oop/python-__str__/
        """

        return f"Product: {self.name}, Price: {self.price} EUR"
