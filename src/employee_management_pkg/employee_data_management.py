from .employee import Employee
__employee_list={4564:[36271333288,"CEM","CAN","AHİ MESUT",5557863545,"SATICI"]}

def employee_add(employee:Employee):
    __employee_list[employee.unique_id]=[employee.trid,employee.name,employee.surname,employee.address,employee.phone,employee.job]

def employee_delete(unique_id:int):
    __employee_list.pop(unique_id)

def employee_get_uniqueid(unique_id:int) -> Employee: 
    return __employee_list[unique_id] 

def employee_get_trid(tckn:int):
    for employee in __employee_list.items():
        if employee[0] == tckn:
            return employee
    return None

def employee_list() -> Employee:
    return __employee_list

def employee_edit(employee:Employee):
    __employee_list[employee.unique_id] = employee