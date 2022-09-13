from .car import Car 

__car_list={4563:["A123-4567","TOYOTA","COROLLA",80000,"BLUE",1600]} 

def add_car(car:Car): 
    __car_list[car.unique_id]=[car.serial_number,car.make,car.model,car.price,car.colour,car.engine_capacity] 

def delete_car(unique_id:int):
    __car_list.pop(unique_id) 

def get_car_with_unique_id(unique_id:int) -> Car: 
    return __car_list[unique_id] 

def brng_car_with_serial_number(serial_number:str) -> Car: 
    for car in __car_list.items():
        if car[0] == serial_number:
            return car
    return None

def list_car() -> Car: 
    return __car_list

def edit_car(car:Car):
    __car_list[car.unique_id]=car