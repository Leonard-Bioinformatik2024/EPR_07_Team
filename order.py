"""This module contains the class Order.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


class Order:
    """Contains methods to mark an order with an id.
    """
    # fist order always recieves the id 1
    _id_counter = 1

    def __init__(self, product, special_requests=None):
        # id of the the order instance
        self.id = Order._id_counter
        # next order will recieve an id one higher than the previouse
        # with this the id will continually go up across all tables!
        Order._id_counter += 1

        self.product = product

        # special_requests can be a list
        if special_requests:
            self.special_requests = special_requests
        else:
            self.special_requests = []

    def price(self):
        """Calculates the price including special requests.
        """
        # counts who many strings of "extra" is contained in the list of special requests
        additions = sum(1 for request in self.special_requests if "extra" in request)
        return self.product.price + additions

    def __str__(self):
        """source: https://www.pythontutorial.net/python-oop/python-__str__/
        """
        special_request_string = ", ".join(self.special_requests)
        return f"Order ID: {self.id}, Product: {self.product.name}, \
Price: {self.price()} EUR, Special request: {special_request_string}"
