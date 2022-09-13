from .customer import Customer
from . import customer_data_management
import re

def __validate_customer(customer: Customer) -> (bool,str):
    pattern     = "[1-9]{1}[0-9]{10}"
    result       = re.search(pattern, customer.trid)
    pattern2    = "[1-9]{1}[0-9]{9}"
    result2      = re.search(pattern2, customer.phone)
    if result == None:
        return (False, "TR ID Must Be 11 Digits!")

    if result == "[0]{1}[0-9]{10}":
        return (False, "TR ID Doesn't Start With '0'!")
    
    if customer_data_management.customer_get_trid(customer.trid) != None:
        return (False, "{customer.tckn} Customer TR ID Number is Used Before!")
    
    if customer.trid.isnumeric() != True:
        return (False, "TR ID Number Must Be Number!")
    
    if result2 == None:
        return (False, "Invalid Phone Number!")

    if customer.phone.isnumeric() != True:
        return (False, "Phone Number Must Be Number!")

    return (True, "Customer Validated")

def add_customer(customer:Customer) -> (bool,str):
    try:
        validation_result = __validate_customer(customer)

        if validation_result[0] == False:
            return validation_result
        
        customer_data_management.customer_add(customer)

        return (True, "Customer Successfully Added.")
    except Exception as ex:
        return (False, "Exception Occurred : " + ex.__str__())        

def list_customer() -> {Customer}:
    return customer_data_management.customer_list()

def delete_customer(unique_id: int) -> bool:
    try:
        customer_data_management.customer_delete(unique_id)
    except:
        return False

def edit_customer(customer:Customer) -> (bool,str):
    try:
        validation_result = __validate_customer(customer)

        if validation_result[0] == False:
            return validation_result

        customer_data_management.customer_edit(customer)[customer.unique_id]=customer

        return (True, "Customer Successfully Added.")
    except Exception as ex:
        return (False, "Exception Occurred : " + ex.__str__())
    
def get_customer(unique_id: int) -> Customer:
    try:
        return customer_data_management.customer_get_uniqueid(unique_id)
    except:
        return Customer()
