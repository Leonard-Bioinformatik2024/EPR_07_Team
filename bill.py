"""This module contains the class Bill.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from datetime import datetime

class Bill:
    """This class contains a method to create a bill for the orders of agiven table.
    """

    def __init__(self, table):
        self.table = table
        self.date = datetime.now()
        self.total = self.table.total_price()

    def create_bill(self):
        """Saving the bill to a .txt file."""


        billname = f"bill_table_{self.table}_{self.date.strftime('%Y%m%d_%H%M%S')}.txt"


        try:
            with open(billname, "w", encoding="utf-8") as bill:
                bill.write(f"Bill for table {self.table}\n")
                bill.write(f"Date: {self.date.strftime('%d-%m-%y %H:%M:%S')}\n")
                bill.write("Orders:\n")
                for order in self.table:
                    bill.write(f"  {order}\n")
                bill.write(f"\nTotal: {round(self.total, 2)} EUR\n")
            print(f"Bill saved under {billname}")
        except Exception as e:
            print(f"Something went wrong :( -> {e}")
