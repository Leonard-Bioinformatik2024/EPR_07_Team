"""This module contains the class Table.
"""


__author__ = "8532653, Hoffmann, 8488705, Singh"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from order import Order

class Table:
    """Used to create instances that contain a number for identification
    and a list of orders (instances of Order) 
    corresponding to the orders made at the given table instance
    Contains methods to manage the orders at a given table.
    """

    def __init__(self, number):
        # Tablenumber to identify a table instance (e.g. in find_table())
        self.number = number
        # List of Order instances
        self.orders = []

    def add_order(self, order):
        """Add a new order to a table.
        """
        # Checking if the given order is an instance of class order
        # and append it to the list of orders
        if isinstance(order, Order):
            self.orders.append(order)
            print(f"Order added to table {self.number}.")
        else:
            print("invalide order. There is no object of type 'order'!")

    def remove_order(self, order_id):
        """Remove an order via its id.
        """
        # Loop to check if there is an instance of order in the list of orders
        # with a matching id to what is given
        for order in self.orders:
            if order_id == order.id:
                # Remove the order instance from the list
                self.orders.remove(order)
                print(f"Order {order_id} has been removed from table {self.number}.")
                return
        print(f"No order with ID {order_id} found at table {self.number}.")

    def show_orders(self):
        """show orders at a given table.
        """
        # If there are no instances in the list return early
        if not self.orders:
            print(f"There are no orders at table {self.number}.")
            return

        print(f"Orders of table {self.number}:")
        # Loop to print all order instances inside the list
        for order in self.orders:
            # uses the __str__ method of the instance
            # https://www.pythontutorial.net/python-oop/python-__str__/
            print(order)

    def total_price(self):
        """Calculates the total price of all orders at a given table.
        """
        # order.price() includes the chrage for special requests
        total = sum(order.price() for order in self.orders)
        return total
