class Computer:
    """
    Computer's attributes are saved & is available here
    Defining attributes:
    Computer's description, processor_type, hard_drive_capacity, 
    memory, operating_system, year_made, price
    """

    #Constructor of Computer class
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):

        #Making a list of all the attributes
        self.computer = {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price}

    def get_attribute(self, attribute):
        """
        Access attributes of computers 
        """

        #All info on the computer
        if attribute == "all attributes":
            return self.computer
        else:
            #specific attribute of the computer
            return self.computer[attribute]

    def update_attribute(self, attribute, updated_value):
        #Change attribute information
        self.computer[attribute] = updated_value