from .customer import Customer
__customer_list={4565:[32271333288,"CEM","CAN","AHİ MESUT",5557863544]}

def customer_add(customer:Customer):
    __customer_list[customer.unique_id]=[customer.trid,customer.name,customer.surname,customer.address,customer.phone]

def customer_delete(unique_id:int):
    __customer_list.pop(unique_id)

def customer_get_uniqueid(unique_id:int) -> Customer: 
    return __customer_list[unique_id] 

def customer_get_trid(tckn:int):
    for customer in __customer_list.items():
        if customer[0] == tckn:
            return customer
    return None

def customer_list() -> Customer:
    return __customer_list

def customer_edit(customer:Customer):
    __customer_list[customer.unique_id] = customer