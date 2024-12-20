"""This is an order and billing system for a restaurant.
"""


__author__ = "8532653, Hoffmann, 8488705, Singh"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from restaurant import Restaurant
from order import Order
from bill import Bill


def main():
    """Using methods of the classes from imported modules to create an OMS.
    """

    print("Order-Management-System")

    # Create instance of Restaurant
    restaurant = Restaurant()

    # Use load_products from the instance Restaurant to create a list of all available products
    restaurant.load_products()

    # Loop for multiple inputs
    while True:
        # Printing the menue options
        print("\nMain Menue")
        print("1. Create new table")
        print("2. Show tables")
        print("3. Remove table")
        print("4. Take order")
        print("5. Show orders")
        print("6. Remove order")
        print("7. Create bill")
        print("8. Exit OMS")

        # Loop for choosing main menue options
        while True:
            options = ['1', '2', '3', '4', '5', '6', '7', '8']
            option = input("Choose an option [1-8]: ")
            if option in options:
                break
            print('invalide input')

        # 1. Create new table
        if option == "1":
            # Loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            restaurant.add_table(tablenumber)
            print(f"Table {tablenumber} added.")

        # 2. Show tables
        elif option == "2":
            if not restaurant.tables:
                print("There are no occupied tables.")
                continue
            # Using show_orders() from the given Table instance to print all orders present inside
            restaurant.show_tables()

        # 3. Remove tables
        elif option == "3":
            # Loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # Uses remove_table() from Restaurant to remove the given table instance
            # from the list of table instances.
            restaurant.remove_table(tablenumber)

        # 4. Take order
        elif option == "4":
            # Loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # Recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue

            # Recieves the given product instance through find_product()
            productname = input("Enter the name of the product: ")
            product = restaurant.find_product(productname)
            if not product:
                print("Product not found.")
                continue

            special_requests = input("Enter special requests (use comma as seperator): ").split(",")
            # Create a clean list from input
            # https://www.datacamp.com/tutorial/python-trim?dc_referrer=https%3A%2F%2Fwww.google.com%2F
            special_requests = [sr.strip() for sr in special_requests if sr.strip()]

            # Passing in the product instance and the list of special requests
            # to create an instance of Order and add it the the list of orders
            # inside the table instance chosen before.
            order = Order(product, special_requests)
            table.add_order(order)
            print("Order was recorded.")

        # 5. Show orders
        elif option == "5":
            # Loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # Recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue
            # Using show_orders() from the given Table instance to print all orders present inside
            table.show_orders()

        # 6. Remove order
        elif option == "6":
            # Loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # Recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue
            # remove the Order instance inside the Table instance corresponding to the given id
            order_id = int(input("Enter the id of the Order you want to remove: "))
            table.remove_order(order_id)

        # 7. Create bill
        elif option == "7":
            # Loop to enter a tablenumber
            while True:
                try:
                    tablenumber = int(input("Enter the tablenumber: "))
                    break
                except ValueError:
                    print("invalide input")
            # Recieves the given table instance through find_table()
            table = restaurant.find_table(tablenumber)
            if not table:
                print("Table not found.")
                continue
            # Creates an instance of Bill
            bill = Bill(table)
            # Using create_bill() from the Bill instance to save a txt-file,
            # which contains all orders at the given Table instance and the total price.
            bill.create_bill()
            print(f"Created and saved bill for table {tablenumber}.")

        # 8. Exit OMS
        elif option == "8":
            print("Closing OMS.")
            break # Breaks the main menue loop and closes the program

if __name__ == "__main__":
    main()
