from .employee import Employee
from . import employee_data_management
import re

def __validate_employee(employee: Employee) -> (bool,str):
    pattern     = "[1-9]{1}[0-9]{10}"
    result       = re.search(pattern, employee.trid)
    pattern2    = "[1-9]{1}[0-9]{9}"
    result2      = re.search(pattern2, employee.phone)
    if result == None:
        return (False, "TR ID Must Be 11 Digits!")

    if result == "[0]{1}[0-9]{10}":
        return (False, "TR ID Doesn't Start With '0'!")
    
    if employee_data_management.employee_get_trid(employee.trid) != None:
        return (False, "{employee.tckn} Employee TR ID Number is Used Before!")
    
    if employee.trid.isnumeric() != True:
        return (False, "TR ID Number Must Be Number!")
    
    if result2 == None:
        return (False, "Invalid Phone Number!")

    if employee.phone.isnumeric() != True:
        return (False, "Phone Number Must Be Number!")

    return (True, "Employee Validated")

def add_employee(employee:Employee) -> (bool,str):
    try:
        validation_result = __validate_employee(employee)

        if validation_result[0] == False:
            return validation_result
        
        employee_data_management.employee_add(employee)

        return (True, "Employee Successfully Added.")
    except Exception as ex:
        return (False, "Exception Occurred : " + ex.__str__())        

def list_employee() -> {Employee}:
    return employee_data_management.employee_list()

def delete_employee(unique_id: int) -> bool:
    try:
        employee_data_management.employee_delete(unique_id)
    except:
        return False

def edit_employee(employee:Employee) -> (bool,str):
    try:
        validation_result = __validate_employee(employee)

        if validation_result[0] == False:
            return validation_result

        employee_data_management.employee_edit(employee)[employee.unique_id]=employee

        return (True, "Employee Successfully Added.")
    except Exception as ex:
        return (False, "Exception Occurred : " + ex.__str__())
    
def get_employee(unique_id: int) -> Employee:
    try:
        return employee_data_management.employee_get_uniqueid(unique_id)
    except:
        return Employee()
