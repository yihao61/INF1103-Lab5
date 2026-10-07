import os
import json

FILEPATH = "inventory.json"

def add_product(inv):
    Adding = True
    progress = 0
    newprod = {}
    print("Add New Product")
    while Adding:
        if progress == 0:
            idinp = input("Product ID: ")
            skip = False
            for item in inv:                
                if idinp == item["id"]:
                    print("ID already exits. Please pick a new one.")
                    skip = True
                    break
            if skip:
                continue

            newprod["id"] = idinp
            progress+=1

        elif progress == 1:
            nameinp = input("Product Name: ")
            newprod["name"] = nameinp
            progress+=1

        elif progress == 2:
            priceinp = input("Price: ")
            try:
                validp = float(priceinp)
            except ValueError:
                print("Not a number. Try Again")
                continue
    
            newprod["price"] = validp
            progress+=1

        elif progress == 3:
            stockinp = input("Stock Quantity: ")

            try:
                valids = int(stockinp)
            except ValueError:
                print("Not a integer. Try Again!")
                continue
    
            newprod["stock"] = valids
            progress+=1
        else:
            print("\nProduct added successfully!")
            Adding = False
            
    inv.append(newprod)
    return inv

def update_stock(inv):
    print("\nUpdate Stock")
    idinp = input("Enter Product ID: ")
    for dict in inv:
        if idinp == dict["id"]:
            print(f"\nProduct Found:\nName: {dict['name']}\nCurrent Stock: {dict['stock']}\n")
            while True:
                usrinp = input("New Stock Quantity: ")
                try:
                    validn = int(usrinp)
                    dict["stock"] = validn
                    print("\nStock updated successfully!")
                    break
                except ValueError:
                    print("Invalid Stock Quantity Entered! Try Again.")
    
    
    return inv

def search_product(inv):
    found = False
    print("\nSearch Product")
    idinp = input("Enter Product ID: ")

    for dict in inv:
        if dict["id"] == idinp:
            print("\nProduct Found!")
            print("------------------------------------------------")
            print(f"ID: {dict['id']}\nName: {dict['name']}\nPrice: ${dict['price']}\nStock: {dict['stock']}")
            print("------------------------------------------------")
            found = True

    if not found:
        print("Product no found")
    
    return

def display_all(inv):
    print("\nCurrent Inventory\n"
          "------------------------------------------------")
    for dict in inv:
        print(f"ID: {dict['id']} | Name: {dict['name']} | Price: ${dict['price']} | Stock: {dict['stock']}")
    print("------------------------------------------------")
    return


def get_valid_input():
    while True:
        try:
            user = input("\nEnter option: ")
            value = int(user)
            if 1 <= value <= 6:
                return value

            print("Number Out of range! Please choose options 1-6.")
        except ValueError:
            print("Invalid Option entered, please try again.")


def load_inventory():
    inv_list = []

    if not os.path.exists(FILEPATH):

        print(f"{FILEPATH} does not exists, creating a blank file...")
        with open(FILEPATH, "w", encoding="utf-8") as file:
            pass
        return inv_list

    
    with open(FILEPATH, "r", encoding="utf-8") as file:
        print(f"{FILEPATH} found.")
        inv_list = json.load(file)

    print("Inventory loaded successfully!")
    return inv_list
    

def save_inventory(inv_list):
    print("\nSaving inventory.....")

    with open(FILEPATH, "w", encoding="utf-8") as file:
        json.dump(inv_list, file, indent=4)

    print("Inventory Saved.....\n")
    return

def main():
    print("============================================================\n"
            "INVENTORY MANAGEMENT SYSTEM\n"
            "============================================================\n")

    inventory = load_inventory()
    exit_program = False

    print("\n----------- MENU -----------"
            "\n1. Display All Products"
            "\n2. Add Product"
            "\n3. Update Stock"
            "\n4. Search Product"
            "\n5. Save Inventory"
            "\n6. Exit"
            "\n----------------------------")

    while not exit_program:
        option = get_valid_input()
        match option:
            case 1:
                display_all(inventory)
            case 2:
                inventory = add_product(inventory)
            case 3:
                update_stock(inventory)
            case 4:
                search_product(inventory)
            case 5:
                save_inventory(inventory)
            case 6:
                exit_program = True

    save_inventory(inventory)
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")



if __name__ == "__main__":
    main()