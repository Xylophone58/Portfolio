# @author Zach Mitchell
# This program process an inventory and allows purchases to be made.
def main():
    SHOW_ITEM_INFORMATION = "1"
    BUY_ITEM = "2"
    QUIT = "3"
    # Create 3 empty, single-dimensions lists for variables named names,
    # prices, and quantities
    names = []
    prices = []
    quantities = []
    # Call the function named get_inventory with "inventory.txt", and the
    # names, prices, and quantities empty lists
    get_inventory("inventory.txt", names, prices, quantities)
    choice = 1
    while choice != QUIT:
        print("=========================")
        print("(1) Show Item Information")
        print("(2) Buy Item")
        print("(3) Quit")
        # Prompt for and get the user choice (string) by storing into
        # the choice variable (Do not convert to an integer)
        choice = input("Choice: ")
        # Process the menu choice
        if choice == SHOW_ITEM_INFORMATION:
            search_name = str(input("Item name? "))
            # You will need to prompt for the item name and store the
            # index returned from a call to search_names with names list
            # and the name which the user just entered.
            for i in range(len(names)):
                if names[i] == search_name:
                    print("Price: " + str(prices[i]))
                    print("Quantity: " + str(quantities[i]))
                    break
                elif names[i] != search_name:
                    print("Item not found")
            # If the name is found, show the item's price
            # and the quantity in stock (Remember, they are
            # parallel arrays and you just found the index.), else
            # display that the item is not found.
        elif choice == BUY_ITEM:
            buy_item_name = str(input("Item name? "))
            # You will need to prompt for the item name and store the
            # index returned from a call to search_names with names list
            # and the name which the user just entered.
            for i in range(len(names)):
                if names[i] == buy_item_name:
                    if quantities[i] > 0:
                        print("Purchse Successful")
                        quantities[i] -= 1
                    elif quantities[i] <= 0:
                        print("Out of stock")
            # If the name is found then
            #    check if there is enough quantity in stock. If so,
            #       display that the item is purchased and decrement
            #       the quantity in stock for that item;
            #    else display that the item is sold out.
            # Else display that the item is not found.
        elif choice != QUIT:
            print("Invalid choice entered.")
    # Call save_inventory with "inventory.txt" and the names, prices, and
    # quantities lists. HINT: When building/testing the program, first
    # write to a different file name such as "inventoryNew.txt"; then when
    # you are sure it works and/or ready to submit, change it to
    # inventory.txt

    save_inventory("inventory.txt", names, prices, quantities)

def get_inventory(filename, items, prices, quantities):

    f = open(filename)

    for line in f:
        pieces = line.split(',')
        items.append(pieces[0])
        prices.append(float(pieces[1]))
        quantities.append(int(pieces[2]))
    """
    Read comma-delimited item information into three different parallel lists.
    @param filename The name of the input file
    @param items An empty list that will hold item names
    @param prices An empty list that will hold item prices (floating pt numbers)
    @param quantities An empty list that will hold item quantities (integers)
    """
def search_names(names, name):

    for i in range(len(names)):
        if names[i] == name:
            return i

    return -1
    """
    Perform a case-insensitive linear search for a name in a list of item names.
    Returns the index of the found item name or -1 if not found.
    @param names The list of item names
    @param name The name for which to search
    """
def save_inventory(filename, items, prices, quantities):

    f = open(filename, 'w')

    for i in range(len(items)):
        f.write(str(items[i]) + ", " + str(prices[i]) + ", " + str(quantities[i]) + "\n")
    """
    Write each item's information in comma-delimited form to consecutive
    individual lines in the file indicated by filename.
    @param filename The name of the output file
    @param items A list of item names
    @param prices A list of item prices
    @param quantities A list of item quantities
    """
main()
