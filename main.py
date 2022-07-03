import math

# Main menu function
def menu(menu):

    while True:

        print("--- Please select an option below ---")
        print("1. New order\n2. Complete order \n")

        try:

            selection = int(input())

            if selection == 1:
                new_order(orders)
                break

            elif selection == 2:
                complete_order(orders)
                break

            else:
                print("Please enter a valid number option")
                continue

        except:
            print("Please enter a number")
    
    return

# Function to add new profit entry
def new_order(incomp_orders):

    # Creates the data set for the profit entry which will be appended into the profits list
    order_data = []
    
    print("--- New Order ---")

    order_data.append(str(input("Enter the name of the buyer \n")))
    print("Buyer name is: " + order_data[0])

    # Loop to ensure entry is a float value
    while True:
        try:
            order_data.append(float(input("Enter the cost of the purchase \n")))
            break
        except:
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
                menu(menu)
                return

            if selection == 2:
                break

            else:
                print("Please select 1 or 2")
                continue
        except:
            print("Please enter a number")

    order_data.append(str(input("Date shipped (mm/dd/yyyy) \n")))
    print("Order shipped on: " + order_data[4])

    order_data.append(str(input("Tracking number: \n")))
    print("Tracking number is: " + order_data[5])

    orders.append(order_data) # Creates an entry in the completed orders list
    
    menu(menu)
    return
    

# Function to complete order information after shipped
def complete_order(orders):
    print("placeholder")



# Setting default values
incomp_orders = []
orders = []
num_incompleted = 0
num_completed = 0

# Begin program by running menu
menu(menu)

print(str(orders))
print("---___---___---")
print(str(incomp_orders))