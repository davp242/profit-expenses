import math

# Main menu function
def menu():

    while True:

        print("--- Please select an option below ---")
        print("1. New order\n2. Complete order")

        try:

            selection = int(input())

            if selection == 1:
                new_order(incomp_orders)
                break

            elif selection == 2:
                complete_order(incomp_orders)
                break

            else:
                print("Please enter a valid number option")
                continue

        except ValueError:
            print("Please enter a number")
    
    return

# Function to add new order
def new_order(incomp_orders):

    # Creates the data set for the order entry which will be appended into the orders list
    order_data = []
    
    print("--- New Order ---")

    order_data.append(str(input("Enter the name of the buyer \n")))
    print("Buyer name is: " + order_data[0])

    # Loop to ensure entry is a float value
    while True:
        try:
            order_data.append(float(input("Enter the cost of the purchase \n")))
            break
        except ValueError:
            print("Please enter in just numbers and decimals (ie 123.12)")

    print("Order cost was $" + str(order_data[1]))
    
    order_data.append(str(input("Mailing address \n")))
    print("Mailing address is: " + order_data[2])

    order_data.append(str(input("Date ordered (mm/dd/yyyy) \n")))
    print("Order date was: " + order_data[3])

    # Loop to allow selection of returning to main menu or entering ship date/tracking number immediately
    while True:
        print("Would you like to enter shipping date/tracking number now or return to main menu?")
        print("1: Menu\n2: Complete order information now")
        try:
            selection = int(input())
            if selection == 1:
                incomp_orders.append(order_data) # Appends list of incompleted orders
                menu()
                return

            if selection == 2:
                break

            else:
                print("Please select 1 or 2")
                continue
        except ValueError:
            print("Please enter a number")

    order_data.append(str(input("Date shipped (mm/dd/yyyy) \n")))
    print("Order shipped on: " + order_data[4])

    order_data.append(str(input("Tracking number: \n")))
    print("Tracking number is: " + order_data[5])

    orders.append(order_data) # Creates an entry in the completed orders list
    
    menu()
    return
    

# Function to complete order information after shipped
def complete_order(incomp_orders):
    print("placeholder selected " + incomp_orders[0])

# Function to select an order to complete
def select_order(incomp_orders):

    # Resets the list to print all the incomplete orders
    order_number = 0
    print("Whose order would you like to complete\n")
    while order_number < int(len(incomp_orders)):
         print(str(order_number + 1) + ": " + str(incomp_orders[order_number][0]))
         order_number += 1

    while True:
        try:
            selection = (int(input("\nEnter the number next to the name of the order you want to complete\n")) - 1)
            complete_order(incomp_orders[selection])
        except ValueError:
            print("Please enter a valid number")

# Setting default values
incomp_orders = []
orders = []
num_incomplete = 0
num_completed = 0

# Begin program by running menu
menu()

print(str(orders))
print("---___---___---")
print(str(incomp_orders))