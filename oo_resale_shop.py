from typing import Dict, Union, Optional
from computer import *
class ResaleShop:

    # What attributes will it need?

    """ inventory: a dictionary where we'll store our inventory
    The key is an int representing the item number
    The value is another dictionary containing information about the machine
    """
    # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.itemID = 0 


    # What methods will you need?
    # Import a few useful containers from the typing module

    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer

        # Add it to the resale store's inventory
        print("Buying", computer.get_attribute("description"))
        print("Adding to inventory...")
        print("Done.\n")
        return self.itemID

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        print("Selling Item ID:", item_id)
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        print("Checking inventory...")
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[self.itemID]}')
        else:
            print("No inventory to display.")
        print("Done.\n")

    def refurbish(self, item_id, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            print("Refurbishing Item ID:", item_id, ", updating OS to", new_os)
            print("Updating inventory...")
            if int(computer.get_attribute("year_made")) < 2000:
                computer.update_attribute("price", 0) # too old to sell, donation only
            elif int(computer.get_attribute("year_made")) < 2012:
                computer.update_attribute("price", 250) # heavily-discounted price on machines 10+ years old
            elif int(computer.get_attribute("year_made")) < 2018:
                computer.update_attribute("price", 550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_attribute("price", 1000) # recent stuff

            if new_os is not None:
                computer.update_attribute("operating_system", new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
        print("Done.\n")