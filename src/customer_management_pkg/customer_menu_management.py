import menu_management
from .customer import Customer
from . import customer_management
import random
import os
import time

__menu =("""
            ===========================
            Customer Management Menu
            ===========================
            Please Select:
            (1) Add Customer
            (2) List Customer
            (3) Delete Customer
            (4) Edit Customer
            (5) Main Menu
            ===========================
            """)

def __add_customer(customer:Customer):
    if customer == None:
        customer_unique_id   = random.randint(1, 1000000)
        customer_trid            = input("Please Input Customer TR ID Number : ")
        customer_name             = input("Please Input Customer Name : ")
        customer_surname          = input("Please Input Customer Surname : ")
        customer_address          = input("Please Input Customer Address : ")
        customer_phone        = input("Please Input Customer Phone Number Without Start With '0' : ")
        customer = Customer(customer_unique_id, customer_trid, customer_name, customer_surname, customer_address, customer_phone)

        result = customer_management.add_customer(customer)

        if result[0] == False:
            print(result[1])
            __add_customer(customer)
        else:
            print("Customer Successfully Added.") 
    
    else:
        print("Please Press Enter to Accept Default Value.")
        customer_trid        = input(f"Please Input Customer TR ID Number : ({customer.trid}) : ")
        customer_name         = input(f"Please Input Customer Name : ({customer.name}): ")
        customer_surname      = input(f"Please Input Customer Surname : ({customer.surname}) : ")
        customer_address      = input(f"Please Input Customer Address : ({customer.address}) : ")
        customer_phone    = input(f"Please Input Customer Phone Number Without Start With '0' : ({customer.tel}) : ")

        if customer_trid == "":
            customer_trid = customer.trid
        
        if customer_name == "":
            customer_name = customer.name

        if customer_surname == "":
            customer_surname = customer.surname
        
        if customer_address == "":
            customer_address = customer.address
        
        if customer_phone == "":
            customer_phone = customer.phone

        customer = Customer(customer.unique_id, customer_trid, customer_name, customer_surname, customer_address, customer_phone)

        result = customer_management.add_customer(customer)

        if result[0] == False:
            print(result[1])
            __add_customer(customer)
        else:
            print("Customer Successfully Added.") 

def get_menu(): 
    while True:
        print(__menu)
        secenek = int(input("Customer Management Menu : "))
        if secenek == 1:
            print("Customer Add is Working...")
            time.sleep(1)
            __add_customer(None)
        elif secenek == 2:
            os.system("cls")
            print("Customers are Listing...")
            time.sleep(1)
            customer_listesi = customer_management.list_customer()
            for customer in customer_listesi.items():
                print(customer)
            print(input("Please Any Key to Continue..."))                
        elif secenek == 3:
            os.system("cls")
            print("Customer Delete is Working...")   
            time.sleep(1)               
            customer_listesi = customer_management.list_customer()
            for customer in customer_listesi.items():
                print(customer)
            customer_management.delete_customer(int(input("Please Input Unique Id You Want to Delete Customer : ")))
        elif secenek == 4:
            os.system("cls")
            print("Customer Edit is Working...")   
            time.sleep(1)                     
            customer_listesi = customer_management.list_customer()
            for customer in customer_listesi.items(): 
                print(customer)
            customer_management.edit_customer(int(input("Please Input Unique Id You Want to Edit Customer : ")))
        elif secenek == 5:
            menu_management.main_menu()
        else:
            print("Please Select Valid Choice!")              
            