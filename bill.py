"""This module contains the class Bill.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from datetime import datetime

class Bill:
    """This class contains a method to create a bill for the orders of agiven table.
    """

    def __init__(self, table):
        # number of the Table instance for which a bill needs to be created
        self.table = table
        # current date and time
        self.date = datetime.now()
        # using a Table method to calculate the total price
        self.total = self.table.total_price()

    def create_bill(self):
        """Saving the bill to a .txt file.
        """
        # creating the name of the bill using number of the selected table object 
        # and the datetime module
        billname = f"bill_table_{self.table.number}_{self.date.strftime('%d%m%y_%H%M%S')}.txt"

        # building the bill using f-strings
        try:
            with open(billname, "w", encoding="utf-8") as bill:
                bill.write(f"Bill for table {self.table.number}\n")
                bill.write(f"Date: {self.date.strftime('%d-%m-%y %H:%M:%S')}\n")
                bill.write("Orders:\n")
                # write the __str__ method of each Order instance in this Table instance
                for order in self.table.orders:
                    bill.write(f"  {order}\n")
                bill.write(f"\nTotal: {round(self.total, 2)} EUR\n")
            print(f"Bill saved under {billname}")

        # pylint does not like this, but it helped with debugging :P
        except Exception as e:
            print(f"Something went wrong :( -> {e}")
