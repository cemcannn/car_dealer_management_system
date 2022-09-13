from car_management_pkg import car_menu_management 
from customer_management_pkg import customer_menu_management 
from employee_management_pkg import employee_menu_management 
from bill_management_pkg import bill_menu_management 


__menu = """ Menu:
                [1] Car Management
                [2] Customer Management 
                [3] Personel Management
                [4] Bill Management
                [5] Exit"""


def main_menu(): 
    while True:
        print(__menu)
        option = int(input("Please select: "))
        if option == 1:
            car_menu_management.get_menu()
        elif option == 2:
            customer_menu_management.get_menu()
        elif option == 3:
            employee_menu_management.get_menu()
        elif option == 4:
            bill_menu_management.get_menu()
        elif option == 5:
            quit()
        else:
            print("Invalid select!")