from car_management_pkg import car
from customer_management_pkg import customer
from employee_management_pkg import employee

class Bill:
    def __init__(self,unique_id: int, no:complex, car: car.Car, customer: customer.Customer, employee: employee.Employee, amount:int, date:int):
        self.unique_id  = unique_id
        self.no             = no    
        self.car           = car
        self.customer        = customer
        self.employee       = employee
        self.amount          = amount
        self.date          = date

    def __str__(self): 
        return f"ID = {self.unique_id}, Bill No = {self.no}, Car = {self.car}, Customer = {self.customer}, Employee = {self.employee}, Bill Amount = {self.amount}, Bill Date = {self.date} "
