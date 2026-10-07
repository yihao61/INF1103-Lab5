import sys
import os
import json

MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10%
FILEPATH = "inventory.json"

def add_product():
    return

def update_stock():
    return

def search_product():
    return

def display_all(inv):
    print("------------------------------------------------")
    for item in inv:
        print(f"ID: {item["ID"]} | Name: {item["Name"]} | Price: {item["Price"]} | Stock: {item["Stock"]}")
    print("------------------------------------------------")
    return


def get_valid_input():
    user = input("Enter option: ")
    while True:
        try:
            value = int(user)
            if 1 <= value <= 6:
                return value

            print("Number Out of range! Please choose options 1-6.")
        except ValueError:
            print("Invalid Option entered, please try again.")


def load_inventory():
    inv_dict = {}

    if not os.path.exists(FILEPATH):

        print(f"{FILEPATH} does not exists, creating a blank file...")
        with open(FILEPATH, "w", encoding="utf-8") as file:
            pass
        return 0, inv_dict

    
    with open(FILEPATH, "r", encoding="utf-8") as file:
        print(f"{FILEPATH} found.")
        inv_dict = json.load(file)

    print("Inventory loaded successfully!")
    return len(inv_dict), inv_dict
    

def save_inventory(inv_dict):
    print("\nSaving inventory.....")

    with open(FILEPATH, "w", encoding="utf-8") as file:
        json.dump(inv_dict, file, indent=4)

    print("Inventory Saved.....\n")
    return

def main():
    inventory = load_inventory()
    exit_program = False
    print("============================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("============================================================")
    while not exit_program:
        option = get_valid_input()
        match option:
            case 1:
                display_all(inventory)
                break
            case 2:
                add_product(inventory)
                break
            case 3:
                update_stock(inventory)
                break
            case 4:
                search_product(inventory)
                break
            case 5:
                save_inventory(inventory)
                break
            case 6:
                exit_program = True

    save_inventory(inventory)
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")



if __name__ == "__main__":
    main()