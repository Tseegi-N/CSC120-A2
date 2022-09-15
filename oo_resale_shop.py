#Import necessary containers from dictionary and computer class
from typing import Dict, Union, Optional
from computer import *

class ResaleShop:
    """
    All resale methods can be found here; all methods will update inventory otw
    Main methods: 
    buy computers, 
    print inventory info, 
    sell computers, 
    refurbish computers,
    update price  
    """

    #Defining attributes
    """ 
    inventory: a dictionary where we'll store our inventory
    The itemID is an int key representing the item number
    The value is another dictionary containing information about the machine
    """

    #Constructor of Resale class
    def __init__(self):
        # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.itemID = 0 
  
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        #Takes in a Dict containing all the information about a computer, 
            #adds it to the inventory, returns the assigned item_id
        self.itemID += 1  #increment itemID

        #Add it to the resale store's inventory
        self.inventory[self.itemID] = computer

        #Print method steps
        print("Buying", computer.get_attribute("description"))
        print("Adding to inventory...")
        print("Done.\n")

        #Return computer ID for reference
        return self.itemID

    def update_price(self, item_id: int, new_price: int):
        """
        Takes in an item_id and a new price, updates the price of the associated
        computer if it is the inventory, prints error message otherwise
        """
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id: int):
        """
        Takes in an item_id, removes the associated computer if it is the inventory, 
        prints error message otherwise
        """
        print("Selling Item ID:", item_id)
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        prints all the items in the inventory (if it isn't empty), prints error otherwise
        """
        print("Checking inventory...")
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[self.itemID].get_attribute("all attributes")}')
        else:
            print("No inventory to display.")
        print("Done.\n")

    def refurbish(self, item_id, new_os: Optional[str] = None):
        """
        Takes in an item_id and new OS, changes associated price and updates OS 
        if item is in the inventory, prints error message otherwise        
        """
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.get_attribute("year_made")) < 2000:
                computer.update_attribute("price", 0) # too old to sell, donation only
            elif int(computer.get_attribute("year_made")) < 2012:
                computer.update_attribute("price", 250) # heavily-discounted price on machines 10+ years old
            elif int(computer.get_attribute("year_made")) < 2018:
                computer.update_attribute("price", 550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_attribute("price", 1000) # recent stuff

            #if new OS is provided, it gets updated
            if new_os is not None:
                print("Refurbishing Item ID:", item_id, ", updating OS to", new_os)
                print("Updating inventory...")
                computer.update_attribute("operating_system", new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.") #error message
        print("Done.\n")