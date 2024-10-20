account_balance = 0.0
warehouse_inventory = {}
operations_history = []


def display_commands():
    print("\nAvailable commands:")
    print("balance - Add or subtract from account balance")
    print("sale - Record a sale")
    print("purchase - Record a purchase")
    print("account - Show current account balance")
    print("list - Show all products in warehouse")
    print("warehouse - Show the status of a specific product")
    print("review - Review operations within a range")
    print("end - Exit the program")


def balance():
    global account_balance
    try:
        amount = float(input("Enter amount to add or subtract from balance: "))
        account_balance += amount
        operations_history.append(f"Balance adjustment: {amount}")
        print(f"Balance updated. New balance: {account_balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def sale():
    global account_balance, warehouse_inventory
    try:
        product_name = input("Enter the product name: ")
        price = float(input(f"Enter the sale price for {product_name}: "))
        quantity = int(input(f"Enter the quantity of {product_name} sold: "))

        if product_name not in warehouse_inventory or warehouse_inventory[product_name]["quantity"] < quantity:
            print(f"Not enough {product_name} in stock to complete the sale.")
            return

        warehouse_inventory[product_name]["quantity"] -= quantity
        account_balance += price * quantity
        operations_history.append(f"Sale: {product_name}, Quantity: {quantity}, Total: {price * quantity:.2f}")
        print(f"Sale recorded. New balance: {account_balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def purchase():
    global account_balance, warehouse_inventory
    try:
        product_name = input("Enter the product name: ")
        price = float(input(f"Enter the purchase price for {product_name}: "))
        quantity = int(input(f"Enter the quantity of {product_name} purchased: "))
        total_cost = price * quantity

        if account_balance < total_cost:
            print("Not enough balance to complete the purchase.")
            return

        account_balance -= total_cost
        if product_name in warehouse_inventory:
            warehouse_inventory[product_name]["quantity"] += quantity
        else:
            warehouse_inventory[product_name] = {"price": price, "quantity": quantity}

        operations_history.append(f"Purchase: {product_name}, Quantity: {quantity}, Total: {total_cost:.2f}")
        print(f"Purchase recorded. New balance: {account_balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def show_account_balance():
    print(f"Current account balance: {account_balance:.2f}")


def list_inventory():
    if not warehouse_inventory:
        print("Warehouse is empty.")
    else:
        print("Current warehouse inventory:")
        for product, details in warehouse_inventory.items():
            print(f"Product: {product}, Price: {details['price']:.2f}, Quantity: {details['quantity']}")


def check_warehouse():
    product_name = input("Enter the product name: ")
    if product_name in warehouse_inventory:
        product = warehouse_inventory[product_name]
        print(f"Product: {product_name}, Price: {product['price']:.2f}, Quantity: {product['quantity']}")
    else:
        print(f"No such product {product_name} in warehouse.")


def review_operations():
    try:
        start = input("Enter the start index (leave empty to start from the beginning): ")
        end = input("Enter the end index (leave empty to go until the end): ")

        start = int(start) if start else 0
        end = int(end) if end else len(operations_history)

        if start < 0 or end > len(operations_history) or start > end:
            print("Invalid range. Please enter valid indices.")
            return

        print(f"Reviewing operations from {start} to {end}:")
        for i in range(start, end):
            print(operations_history[i])
    except ValueError:
        print("Invalid input. Please enter valid indices.")


def main():
    display_commands()
    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == "balance":
            balance()
        elif command == "sale":
            sale()
        elif command == "purchase":
            purchase()
        elif command == "account":
            show_account_balance()
        elif command == "list":
            list_inventory()
        elif command == "warehouse":
            check_warehouse()
        elif command == "review":
            review_operations()
        elif command == "end":
            print("Terminating the program.")
            break
        else:
            print("Invalid command. Please try again.")
        display_commands()


if __name__ == "__main__":
    main()
