import menu_management
from bill_management_pkg import bill_data_management as bdm
from customer_management_pkg import customer_data_management as cdm
from employee_management_pkg import employee_data_management as edm
from .bill import Bill
from . import bill_management
import random
import time
import os

__menu =("""
            ===========================
            Bill Management Menu
            ===========================
            Please Select:
            (1) Add Bill
            (2) List Bill
            (3) Delete Bill
            (4) Edit Bill
            (5) Main Menu
            ===========================
            """)

def __add_bill(bill:Bill):
    if bill == None:
        bill_unique_id            = random.randint(1, 1000000)
        bill_no                       = input("Please Input Bill Number Like 'AAA2021000000' Pattern Example: ")
        os.system("cls")
        print(bdm.list_bill())
        bill_bill                     = bdm.get_bill_with_unique_id(int(input("Please Input Bill Unique Id : ")))
        os.system("cls")
        print(cdm.list_customer())
        os.system("cls")
        bill_customer                  = cdm.get_customer_with_unique_id(int(input("Please Input Customer Unique Id : ")))
        print(edm.list_employee())
        bill_employee                 = edm.get_employee_with_unique_id(int(input("Please Input Employee Unique Id : ")))
        bill_amount                   = bill_management.__calculate_tax(bill_bill)
        bill_date                   = time.datetime.now()
        bill = Bill(bill_unique_id, bill_no, bill_bill, bill_customer, bill_employee, bill_amount, bill_date)

        result = bill_management.add_bill(bill)

        if result[0] == False:
            print(result[1])
            __add_bill(bill)
        else:
            print("Bill Successfully Added.") 
    
    else:
        print("Please Press Enter to Accept Default Value.")
        bill_no                       = input(f"Please Input Bill Number Like 'AAA2021000000' Pattern Example({bill.no}) : ")
        os.system("cls")
        print(bdm.list_bill())
        bill_bill                     = bdm.get_bill_with_unique_id(int(input("Please Input Bill Unique Id ({bill.bill}): ")))
        os.system("cls")        
        print(cdm.list_customer())
        bill_customer                  = cdm.get_customer_with_unique_id(int(input("Please Input Customer Unique Id ({bill.customer}): ")))
        os.system("cls")
        print(edm.list_employee())
        bill_employee                 = edm.get_employee_with_unique_id(int(input("Please Input Employee Unique Id({bill.employee}): ")))
        bill_amount                   = bill_management.__calculate_tax(bill_bill)
        bill_date                   = time.datetime.now()

        if bill_no == "":
            bill_no = bill.no
        
        if bill_bill == "":
            bill_bill = bill.bill

        if bill_customer == "":
            bill_customer = bill.customer
            
        if bill_employee == "":
            bill_employee = bill.employee
        
        if bill_amount == "":
            bill_amount = bill.amount
        
        if bill_date == "":
            bill_date = bill.date

        bill = Bill(bill.unique_id, bill_no, bill_bill, bill_customer, bill_employee, bill_amount, bill_date)

        result = bill_management.add_bill(bill)

        if result[0] == False:
            print(result[1])
            __add_bill(bill)
        else:
            print("Bill Successfully Added.") 

def get_menu():
    while True:
        print(__menu) 
        option = int(input("Bill Management Menu : "))
        if option == 1: 
            print("Bill Add is Working...")
            time.sleep(1)
            __add_bill(None) 
        elif option == 2: 
            os.system("cls")
            print("Bills are Listing...")
            time.sleep(1)
            bill_list = bill_management.list_bill() 
            for bill in bill_list.items(): 
                print(bill)
            print(input("Please Any Key to Continue..."))
        elif option == 3:
            os.system("cls")
            print("Bill Delete is Working...")   
            time.sleep(1)                     
            bill_list = bill_management.list_bill()
            for bill in bill_list.items(): 
                print(bill)
            bill_management.delete_bill(int(input("Please Input Unique Id You Want to Delete Bill : ")))
        elif option == 4:
            os.system("cls")
            print("Bill Edit is Working...")   
            time.sleep(1)                     
            bill_list = bill_management.list_bill()
            for bill in bill_list.items(): 
                print(bill)
            bill_management.edit_bill(int(input("Please Input Unique Id You Want to Edit Bill : ")))
        elif option == 5:
            menu_management.main_menu()
        else:
            print("Please Select Valid Choice!")