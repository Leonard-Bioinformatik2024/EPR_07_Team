"""This module contains the class Table.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from order import Order

class Table:
    """Contains methods to manage the orders at a given table.
    """

    def __init__(self, number):
        self.number = number
        self.orders = []

    def add_order(self, order):
        """Add a new order to a table.
        """
        if isinstance(order, Order):
            self.orders.append(order)
            print(f"Order added to table {self.number}.")
        else:
            print("invalide order. There is no object of type 'order'!")

    def remove_order(self, order_id):
        """Remove an order via its id.
        """
        for order in self.orders:
            if order_id == order:
                self.orders.remove(order)
                print(f"Order {order_id} has been removed from table {self.number}.")
                return
        print(f"No order with ID {order_id} found at table {self.number}.")

    def total_price(self):
        """Calculates the total price of all orders at a given table.
        """
        total = sum(order.price() for order in self.orders)
        return total

    def show_orders(self):
        """show orders at a given table.
        """
        if not self.orders:
            print(f"There are no orders at table {self.number}.")
            return

        print(f"Orders of table {self.number}:")
        for order in self.orders:
            print(f"  ID: {order.id}, Product: {order.product}, Price: {order.price()} EUR")
