class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    def __init__(self):
        pass

    # What methods will you need?
    def create_computer(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price}      
    """
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):

        self.computer = {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price}

    def get_attribute(self, attribute):
        return self.computer[attribute]

    def update_attribute(self, attribute, updated_value):
        self.computer[attribute] = updated_value
        #self-reference
        #self.description = description
        #self.processor_type = processor_type
        #self.hard_drive_capacity = hard_drive_capacity
        #self.memory = memory
        #self.operating_system = operating_system
        #self.year_made = year_made
        #self.price = price


    # What methods will you need?
    def return_description(self):
        return self.description

    def return_processor_type(self):
        return self.processor_type

    def return_hard_drive_capacity(self):
        return self.hard_drive_capacity

    def return_memory(self):
        return self.memory

    def return_operating_system(self):
        return self.operating_system

    def return_year_made(self):
        return self.year_made

    def return_price(self):
        return self.price
    