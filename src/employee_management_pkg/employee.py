class Employee:
    def __init__(self,unique_id: int, trid:int,name:str,surname:str,address:complex,phone:int,job:str):
        self.unique_id      = unique_id
        self.trid           = trid
        self.name           = name
        self.surname        = surname
        self.address        = address
        self.phone          = phone
        self.job            = job

    def __str__(self): 
        return f"ID = {self.unique_id}, TR ID = {self.trid}, Name = {self.name}, Surname = {self.surname}, Address = {self.address}, Phone = {self.phone}, Job = {self.job} "
