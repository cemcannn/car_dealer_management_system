from .bill import Bill
__list_bill=dict()

def add_bill(bill:Bill):
    __list_bill[bill.unique_id]=[bill.no,bill.car,bill.customer,bill.employee,bill.amount,bill.date]

def delete_bill(unique_id:int):
    __list_bill.pop(unique_id)

def get_bill_with_unique_id(unique_id:int) -> Bill: 
    return __list_bill[unique_id] 

def get_bill_with_bill_no(no:complex):
    for bill in __list_bill.items():
        if bill[0] == no:
            return bill
    return None

def list_bill() -> Bill:
    return __list_bill

def edit_bill(bill:Bill):
    __list_bill[bill.unique_id] = bill