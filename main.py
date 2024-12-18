"""This is an order and billing system for a restaurant.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from restaurant import Restaurant
from order import Order
from bill import Bill


def main():
    """Using methods of the classes from imported modules to create an OMS.
    """

    print("Order-Management-System")

    # create instance of Restaurant
    restaurant = Restaurant()

    # use load_products from the instance Restaurant to create a list of all available products
    restaurant.load_products()

    # loop for multiple inputs
    while True:
        print("\nMain Menue")
        print("1. Create new table")
        print("2. Take order")
        print("3. Remove order")
        print("4. Show orders")
        print("5. Create bill")
        print("6. Exit OMS")

        while True:
            options = ['1', '2', '3', '4', '5', '6']
            option = input("Choose an option [1-6]: ")
            if option in options:
                break
            print('invalide input')

        if option == "1":
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            restaurant.add_table(tablenumber)
            print(f"Table {tablenumber} added.")

        elif option == "2":
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue

            productname = input("Enter the name of the product: ")
            product = restaurant.find_product(productname)
            if not product:
                print("Product not found.")
                continue

            special_requests = input("Enter special requests (use comma as seperator): ").split(",")
            # create a clean list from input
            # https://www.datacamp.com/tutorial/python-trim?dc_referrer=https%3A%2F%2Fwww.google.com%2F
            special_requests = [sr.strip() for sr in special_requests if sr.strip()]

            order = Order(product, special_requests)
            table.add_order(order)
            print("Order was recorded.")

        elif option == "3":
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue

            order_id = int(input("Enter the id of the Order you want to remove: "))
            table.remove_order(order_id)

        elif option == "4":
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue

            table.show_orders()

        elif option == "5":
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue

            bill = Bill(table)
            bill.create_bill()
            print(f"Created and saved bill for table {tablenumber}.")

        elif option == "6":
            print("Closing OMS.")
            break

        else:
            print("invalide input")

if __name__ == "__main__":
    main()
