from .bill import Bill
from . import bill_data_management
from . import bill_menu_management as fmy
import re

# Motor silindir hacmi 1600 cm³’ü geçmeyen, matrahı 92 bin TL’ye kadar olan araçların ÖTV oranı %45
# Motor silindir hacmi 1600 cm³’ü geçmeyen, matrahı 92 bin TL ile 150 bin TL arası araçların ÖTV oranı %50
# Motor silindir hacmi 1600 cm³’ü geçmeyen, matrahı 150 bin TL üzeri araçların ÖTV oranı %80
# Motor silindir hacmi 1600 cm³ ile 2000 cm³ arası, matrahı 170 bin TL’ye kadar araçların ÖTV oranı %130
# Motor silindir hacmi 1600 cm³ ile 2000 cm³ arası, matrahı 170 bin TL üzeri araçların ÖTV oranı %150
# 2000 cm³ üzeri motor silindir hacmi olan matrahında sınır olmayan araçların ÖTV oranı %220

def __calculate_tax(bill_car: int) -> (int):
    if bill_car[5] <= 1599 and bill_car[3] <= 91000:
        bill_amount = bill_car[3] * 145 / 100 * 118 / 100  
        return bill_amount
    elif bill_car[5] <= 1599 and bill_car[3] >= 92000 and bill_car[3] <= 149000:
        bill_amount = bill_car[3] * 150 / 100 * 118 / 100  
        return bill_amount
    elif bill_car[5] <= 1599 and bill_car[3] >= 150000:
        bill_amount = bill_car[3] * 180 / 100 * 118 / 100  
        return bill_amount      
    elif bill_car[5] >= 1600 and bill_car[5] <= 1999 and bill_car[3] <= 169000:
        bill_amount = bill_car[3] * 230 / 100 * 118 / 100  
        return bill_amount
    elif bill_car[5] >= 1600 and bill_car[5] <= 1999 and bill_car[3] >= 170000:
        bill_amount = bill_car[3] * 250 / 100 * 118 / 100
        return bill_amount
    elif bill_car[5] >= 2000:
        bill_amount = bill_car[3] * 320 / 100 * 118 / 100  
        return bill_amount

def __validate_bill(bill: Bill) -> (bool,str):
    pattern     = "[A-Z]{3}[2021][0-9]{6}"
    result       = re.search(pattern, bill.no)

    if result == None:
        return (False, "Bill Number is not Valid AAA2021000000 Pattern Example!")
    
    if bill_data_management.get_bill_with_bill_no(bill.no) != None:
        return (False, "{bill.no} Bill Number is used before!")

    return (True, "Bill Validated")

def add_bill(bill:Bill) -> (bool,str):
    try:
        validate_result = __validate_bill(bill)

        if validate_result[0] == False:
            return validate_result
        
        bill_data_management.add_bill(bill)

        return (True, "Bill Successfully Added.")
    except Exception as ex:
        return (False, "Exception Ocurred : " + ex.__str__())        

def list_bill() -> {Bill}:
    return bill_data_management.list_bill()

def delete_bill(unique_id: int) -> bool:
    try:
        bill_data_management.delete_bill(unique_id)
    except:
        return False

def edit_bill(bill:Bill) -> (bool,str):
    try:
        validate_result = __validate_bill(bill)

        if validate_result[0] == False:
            return validate_result

        bill_data_management.edit_bill(bill)[bill.unique_id]=bill

        return (True, "Bill Successfully Added.")
    except Exception as ex:
        return (False, "Exception Ocurred : " + ex.__str__())
    
def get_bill(unique_id: int) -> Bill:
    try:
        return bill_data_management.get_bill_with_unique_id(unique_id)
    except:
        return Bill()
