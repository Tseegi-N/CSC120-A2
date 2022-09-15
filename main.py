""" 
CSC120: Object Oriented Programming 
A2: Tseegi Nyamdorj
Collaborated with Tina Chang
"""

# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

#Import functions from two Objects
from computer import *
from oo_resale_shop import *

def main():
    """
    Create a new computer
    Test out functions of resale shop by utilizing the new computer
    """

    # First, let's make a computer
    computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    shop = ResaleShop() #Creating object of the class ResaleShop
    computer_id = shop.buy(computer) #Call the buy method from shop

    #Call print inventory method to check
    shop.print_inventory()

    #Refurbish method to update OS
    shop.refurbish(computer_id, 
                    "MacOS Monterey")

    #Call print inventory method to check
    shop.print_inventory()
    
    #Sell method to sell the computer
    shop.sell(computer_id)
    
    #Call print inventory method to check
    shop.print_inventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()
