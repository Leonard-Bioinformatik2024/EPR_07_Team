"""This module contains the class Restaurant.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


import pandas as pd

from table import Table
from product import Product


class Restaurant:
    """Containing methods to organize the tables and products.
    """

    def __init__(self):
        self.tables = []
        self.products = []

    def load_products(self):
        """Reads in the products contained in the food.csv file
        and stores the in a list as a touple with its name and price.
        """
        # try to open the file food.csv
        try:
            with open('food.csv', mode='r', encoding='utf-8') as menue:
                df = pd.read_csv(menue, sep=';')
                for row in range(len(df)):
                    product = Product(name=df.values[row][0], price=float(df.values[row][3]))
                    self.products.append(product)
            print("Products loaded successfully.")
            print(self.products)
        # throw Exeptions if the file is not found or the layout of its contents is incorrect.
        except FileNotFoundError:
            print("File not found! Check if the file is named correcly -> food.csv")
        except KeyError:
            print("Faulty csv-file! \
                  Check if 'name' is the first and 'price' the fourth collumn of the table inside.")

    def find_table(self, tablenumber):
        """Find a table through its designated number.
        """
        for table in self.tables:
            if tablenumber == table.number:
                return table
        return None

    def find_product(self, productname):
        """Find a product through its designated name."""
        for product in self.products:
            # convert to lowercase
            if productname.lower() == product.name.lower():
                return product
        return None

    def add_table(self, tablenumber):
        """Add a new table to the list of occupied tables."""
        if self.find_table(tablenumber):
            print(f"Table {tablenumber} is occupied.")
        else:
            new_table = Table(tablenumber)
            self.tables.append(new_table)
