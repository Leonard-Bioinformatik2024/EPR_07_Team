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
        # printing the menue options
        print("\nMain Menue")
        print("1. Create new table")
        print("2. Take order")
        print("3. Remove order")
        print("4. Show orders")
        print("5. Create bill")
        print("6. Exit OMS")

        # loop for choosing main menue options
        while True:
            options = ['1', '2', '3', '4', '5', '6']
            option = input("Choose an option [1-6]: ")
            if option in options:
                break
            print('invalide input')

        # 1. Create new table
        if option == "1":
            # loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            restaurant.add_table(tablenumber)
            print(f"Table {tablenumber} added.")

        # 2. Take order
        elif option == "2":
            # loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue

            # recieves the given product instance through find_product()
            productname = input("Enter the name of the product: ")
            product = restaurant.find_product(productname)
            if not product:
                print("Product not found.")
                continue

            special_requests = input("Enter special requests (use comma as seperator): ").split(",")
            # create a clean list from input
            # https://www.datacamp.com/tutorial/python-trim?dc_referrer=https%3A%2F%2Fwww.google.com%2F
            special_requests = [sr.strip() for sr in special_requests if sr.strip()]

            # passing in the product instance and the list of special requests
            # to create an instance of Order and add it the the list of orders
            # inside the table instance chosen before
            order = Order(product, special_requests)
            table.add_order(order)
            print("Order was recorded.")

        # 3. Remove order
        elif option == "3":
            # loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue
            # remove the Order instance inside the Table instance corresponding to the given id
            order_id = int(input("Enter the id of the Order you want to remove: "))
            table.remove_order(order_id)

        # 4. Show orders
        elif option == "4":
            # loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue
            # using show_orders() from the given Table instance to print all orders present inside
            table.show_orders()

        # 5. Create bill
        elif option == "5":
            # loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue
            # creates an instance of Bill
            bill = Bill(table)
            # Using create_bill() from the Bill instance to save a txt-file,
            # which contains all orders at the given Table instance and the total price.
            bill.create_bill()
            print(f"Created and saved bill for table {tablenumber}.")

        # 6. Exit OMS
        elif option == "6":
            print("Closing OMS.")
            break # breaks the main menue loop and closes the program

if __name__ == "__main__":
    main()
