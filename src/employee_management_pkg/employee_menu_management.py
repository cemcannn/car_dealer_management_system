import menu_management
from .employee import Employee
from . import employee_management
import random
import os
import time

__menu =("""
            ===========================
            Employee Management Menu
            ===========================
            Please Select:
            (1) Add Employee
            (2) List Employee
            (3) Delete Employee
            (4) Edit Employee
            (5) Main Menu
            ===========================
            """)

def __add_employee(employee:Employee):
    if employee == None:
        employee_unique_id   = random.randint(1, 1000000)
        employee_trid            = input("Please Input Employee TR ID Number : ")
        employee_name             = input("Please Input Employee Name : ")
        employee_surname          = input("Please Input Employee Surname : ")
        employee_address          = input("Please Input Employee Address : ")
        employee_phone        = input("Please Input Employee Phone Number Without Start With '0' : ")
        employee_job            = input("Please Input Employee Job : ")
        employee = Employee(employee_unique_id, employee_trid, employee_name, employee_surname, employee_address, employee_phone, employee_job)

        result = employee_management.add_employee(employee)

        if result[0] == False:
            print(result[1])
            __add_employee(employee)
        else:
            print("Employee Successfully Added.") 
    
    else:
        print("Please Press Enter to Accept Default Value.")
        employee_trid        = input(f"Please Input Employee TR ID Number : ({employee.trid}) : ")
        employee_name         = input(f"Please Input Employee Name : ({employee.name}): ")
        employee_surname      = input(f"Please Input Employee Surname : ({employee.surname}) : ")
        employee_address      = input(f"Please Input Employee Address : ({employee.address}) : ")
        employee_phone    = input(f"Please Input Employee Phone Number Without Start With '0' : ({employee.tel}) : ")
        employee_job    = input(f"Please Input Employee Job : ({employee.job}) : ")

        if employee_trid == "":
            employee_trid = employee.trid
        
        if employee_name == "":
            employee_name = employee.name

        if employee_surname == "":
            employee_surname = employee.surname
        
        if employee_address == "":
            employee_address = employee.address
        
        if employee_phone == "":
            employee_phone = employee.phone

        if employee_job == "":
            employee_job = employee.job

        employee = Employee(employee.unique_id, employee_trid, employee_name, employee_surname, employee_address, employee_phone, employee_job)

        result = employee_management.add_employee(employee)

        if result[0] == False:
            print(result[1])
            __add_employee(employee)
        else:
            print("Employee Successfully Added.") 

def get_menu(): 
    while True:
        print(__menu)
        secenek = int(input("Employee Management Menu : "))
        if secenek == 1:
            print("Employee Add is Working...")
            time.sleep(1)
            __add_employee(None)
        elif secenek == 2:
            os.system("cls")
            print("Employees are Listing...")
            time.sleep(1)
            employee_listesi = employee_management.list_employee()
            for employee in employee_listesi.items():
                print(employee)
            print(input("Please Any Key to Continue..."))                
        elif secenek == 3:
            os.system("cls")
            print("Employee Delete is Working...")   
            time.sleep(1)               
            employee_listesi = employee_management.list_employee()
            for employee in employee_listesi.items():
                print(employee)
            employee_management.delete_employee(int(input("Please Input Unique Id You Want to Delete Employee : ")))
        elif secenek == 4:
            os.system("cls")
            print("Employee Edit is Working...")   
            time.sleep(1)                     
            employee_listesi = employee_management.list_employee()
            for employee in employee_listesi.items(): 
                print(employee)
            employee_management.edit_employee(int(input("Please Input Unique Id You Want to Edit Employee : ")))
        elif secenek == 5:
            menu_management.main_menu()
        else:
            print("Please Select Valid Choice!")              
            