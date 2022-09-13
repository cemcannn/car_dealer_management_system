class Car: 
    def __init__(self, unique_id: int, serial_number: str, make: str, model: str, price: int, colour: str, engine_capacity: int):
        self.unique_id  = unique_id
        self.serial_number         = serial_number # pattern A000-0000
        self.make          = make
        self.model          = model
        self.price          = price
        self.colour           = colour #must be integer
        self.engine_capacity       = engine_capacity

    def __str__(self): 
        return f"Car ID = {self.unique_id}, Car Serial Number = {self.serial_number}, Car Make = {self.make}, Car Model = {self.model}, Car Price = {self.price}, Car Engine Capacity = {self.engine_capacity}"

