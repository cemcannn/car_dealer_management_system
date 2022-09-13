from .car import Car 
import re 
from . import car_data_management 


def __validate_car(car:Car) -> (bool,str):

    pattern = "A[0-9]{3}-[0-9]{4}" 
    result = re.search(pattern, car.serial_number) 
    if result == None:
        return (False, "Serial Number is not Valid A000-0000 Pattern Example!")

    if car_data_management.brng_car_with_serial_number(car.serial_number) != None:
        return (False, "Serial Number is Used Before!")

    if type(car.price) != int:
        return (False, "Price Must Be Number!")

    return (True, "Car Validated")


def add_car(car: Car) -> (bool,str):
    # validasyon ve varsa diğer iş kuralları yazılmalı
    try:
        validation_result = __validate_car(car)

        if validation_result[0] == False:
            return  validation_result

        car_data_management.add_car(car)

        return (True, "Car Successfully Added.")
    except Exception as ex:
        return (False, "Exception Ocurred : " +  ex.__str__())

def list_car() -> {Car}:
    return car_data_management.list_car()

def delete_car(unique_id: int) -> bool:
    try:
        car_data_management.delete_car(unique_id)
        print("Car Successfully Deleted.")
    except:
        return False

def edit_car(car: Car) -> (bool, str):
    # validasyon ve varsa diğer iş kuralları yazılmalı
    try:
        validation_result = __validate_car(car)

        if validation_result[0] == False:
            return  validation_result

        car_data_management.edit_car(car)[car.unique_id]=car

        return (True, "Car Successfully Added.")
    except Exception as ex:
        return (False, "Exception Ocurred : " + ex.__str__())


def get_car(unique_id: int) -> Car:
    try:
        return car_data_management.get_car_with_unique_id(unique_id)
    except:
        return Car()

