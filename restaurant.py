"""This module contains the class Restaurant.
"""


__author__ = "8532653, Hoffmann, 8488705, Singh"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


import pandas as pd # Using the pandas library to read the food.csv file

from table import Table
from product import Product


class Restaurant:
    """Containing methods to organize the tables and products.
    """

    def __init__(self):
        # List of table instances
        self.tables = []
        # List of product instances
        self.products = []

    def load_products(self):
        """Reads in the products contained in the food.csv file
        and stores each item in a list as an instance of Product.
        """
        # Try to open the file food.csv
        try:
            with open('food.csv', mode='r', encoding='utf-8') as menue:
                df = pd.read_csv(menue, sep=';')
                # Loop to store each item as an instance of product in the list self.products
                for row in range(len(df)):
                    product = Product(name=df.values[row][0], price=float(df.values[row][3]))
                    self.products.append(product)
            print("Products loaded successfully.")
            # print(self.products)

        # Throw exception if the file is not found
        except FileNotFoundError:
            print("File not found! Check if the file is named correcly -> food.csv")

    def find_product(self, productname):
        """Find a product through its designated name.
        """
        # Loop to check if the given product is present in the list of products
        for product in self.products:
            if productname == product.name: # product.name is the name attribute of the instance
                return product
        return None

    def find_table(self, tablenumber):
        """Find a table through its designated number.
        """
        # Loop to check if the given table is present in the list of tables
        for table in self.tables:
            if tablenumber == table.number: # table.number is the number attribute of the instance
                return table
        return None

    def add_table(self, tablenumber):
        """Add a new table to the list of occupied tables.
        """
        # Use find table
        if self.find_table(tablenumber):
            print(f"Table {tablenumber} already exists.")
        else:
            new_table = Table(tablenumber)
            # Print(new_table)
            self.tables.append(new_table)

    def show_tables(self):
        """Shows the tables from the list of tables.
        Similar to show_orders(), to make it easier to identify a certain table.
        """
        # Checks if there are any tables available.
        if not self.tables:
        # If not, then this will be shown
            print("There are no tables occupied.")
            return
        # If tables are available, then this will be shown
        print("The occupied tables in the system are: ")
        occupied_tables = []
        # Makes a list of the available tables
        for table in self.tables:
            occupied_tables.append(table.number)
        print(occupied_tables)

    def remove_table(self, tablenumber):
        """Removes the table from the list of tables.
        Until now there is no way to remove tables, so the restaurant needs to
        continualy create a new table or remove all the orders from an existing one to reuse it.
        """
        for table in self.tables:
            if tablenumber == table.number:
                # Remove the order instance from the list
                self.tables.remove(table)
                print(f"Table number {tablenumber} is no longer occupied.")
                return
        print(f"No table with number {tablenumber} is occupied.")
