"""This module contains the class Restaurant.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


import pandas as pd # using the pandas library to read the food.csv file

from table import Table
from product import Product


class Restaurant:
    """Containing methods to organize the tables and products.
    """

    def __init__(self):
        # list of Table instances
        self.tables = []
        # list of Product instances
        self.products = []

    def load_products(self):
        """Reads in the products contained in the food.csv file
        and stores each item in a list as an instance of Product.
        """
        # try to open the file food.csv
        try:
            with open('food.csv', mode='r', encoding='utf-8') as menue:
                df = pd.read_csv(menue, sep=';')
                # loop to store each item as an instance of Product in the list self.products
                for row in range(len(df)):
                    product = Product(name=df.values[row][0], price=float(df.values[row][3]))
                    self.products.append(product)
            print("Products loaded successfully.")
            # print(self.products)

        # throw Exeptions if the file is not found
        except FileNotFoundError:
            print("File not found! Check if the file is named correcly -> food.csv")

    def find_product(self, productname):
        """Find a product through its designated name.
        """
        # loop to check if the given product is present in the list of products
        for product in self.products:
            if productname == product.name: # product.name is the name attribute of the instance
                return product
        return None

    def find_table(self, tablenumber):
        """Find a table through its designated number.
        """
        # loop to check if the given table is present in the list of tables
        for table in self.tables:
            if tablenumber == table.number: # table.number is the number attribute of the instance
                return table
        return None

    def add_table(self, tablenumber):
        """Add a new table to the list of occupied tables.
        """
        # use find table
        if self.find_table(tablenumber):
            print(f"Table {tablenumber} already exists.")
        else:
            new_table = Table(tablenumber)
            # print(new_table)
            self.tables.append(new_table)


    # IMPLEMENTED
    def remove_table(self, tablenumber):
        """Removes the table from the list of tables.
        Until now there is no way to remove tables, so the restaurant needs to
        continualy create a new table or remove all the orders from an existing one to reuse it.
        """
         # Tries to find the table
        table = self.find_table(tablenumber)
        if table:
            # If the table is found, it will be removed
            self.tables.remove(table)
            print(f"The table {tablenumber} has been removed")
        else:
            if table not found
            # If table is not found, this will appear
            print(f"The table {tablenumber} has not been found")
        pass # TODO: Check if anything needs to be changed, please 
        
    # IMPLEMENTED
    def show_tables(self):
        """Shows the tables from the list of tables.
        Similar to show_orders(), to make it easier to identify a certain table.
        """
        # Checks if there are any tables available.
        if not self.tables
        # If not, then this will be shown
            print(f"Sorry for the inconvenience but there are no tables available.")
            return
        # If tables are available, then this will be shown
        print("The available tables in the system are: ")
        # Makes a list of the available tables
        for tables in self.tables
            print(f"Tables avialable are {table.number}")
        pass # TODO: Check if anything needs to be changed, please
    
