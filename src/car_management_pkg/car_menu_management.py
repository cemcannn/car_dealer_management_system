from .car import Car 
from . import car_management 
import random 
import menu_management
import os
import time

__menu =("""
            ===========================
            Car Management Menu
            ===========================
            Please Select:
            (1) Add Car
            (2) List Car
            (3) Delete Car
            (4) Edit Car
            (5) Main Menu
            ===========================
            """)

def __add_car(car:Car): # Araç ekle fonksiyonu oluşturup keyword argument olarak car parametresini Car classına eşliyoruz.
    if car==None: # Eğer car parametresi boş ise:
        car_unique_id  = random.randint(1, 1000000) # Arac_benzersiz kod adında bir değişken  tanımlıyoruz sebebi ise aracın unique bir sayıya sahip olması, bunu da rastgele 1 ile 1000000 arasında bir rakamdan seçmesini sağlıyoruz.
        car_serial_number         = input("Please Input Bill Number Like 'A000-0000' Pattern Example: ") # Car seri no değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        car_make          = input("Please Input Car Make : ")  # Car make değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        car_model          = input("Please Input Car Model : ")  # Car model değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        car_price          = input("Please Input Car Price : ")  # Car price değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        car_colour           = input("Please Input Car Colour : ")  # Car renk değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        car_engine_capacity       = input("Please Input Car Engine Capacity : ") 
        car = Car(car_unique_id, car_serial_number, car_make, car_model, int(car_price), car_colour, int(car_engine_capacity)) # Car değişkenini Car classına eşitliyoruz.

        result = car_management.add_car(car) # Sonuç değişkenine car yonetimi dosyasında car ekle fonksiyonunu çalıştırıp oluşturduğumuz car değişkenini ekliyoruz.

        if result[0] == False: # Eğer result değişkeninin 0'ıncı indeksi False ise
            print(result[1]) # Sonuç değişkeninin 1. indeksi yazdırılır
            __add_car(car) # Yukarıda eklenen car ekle fonksiyonuna car parametresi eklenir
        else:
            print("Car Successfully Added.") # Burayı tam anlamadım

    else:
        print("Please Press Enter to Accept Default Value.")
        car_serial_number     = input(f"Lütfen Araç Seri Numarasını 'A000-0000' Pattern Örneğine göre Giriniz ({car.serial_number}):") # Eğer araç seri nosu araç paternine uymuyorsa bizden tekrar seri no istiyor ve araç seri no yazdırıyor.
        car_make      = input(f"Please Input Car Make ({car.make}): ")
        car_model      = input(f"Please Input Car Model ({car.model}): ")
        car_price      = input(f"Please Input Car Price ({car.price}): ")
        car_colour       = input(f"Please Input Car Colour ({car.renk}): ")
        car_engine_capacity   = input("Please Input Car Engine Capacity ({car.engine_capacity}): ") 

        if car_serial_number == "": # Eğer bir değer vermezsek arac_seri noyu eski değer olarak bırakır.
            car_serial_number = car.serial_number

        if car_make == "":
            car_make = car.make

        if car_model == "":
            car_model = car.model

        if car_price == "":
            car_price = car.price

        if car_colour == "":
            car_colour = car.colour

        if car_engine_capacity == "":
            car_engine_capacity = car.engine_capacity

        car = Car(car.unique_id, car_serial_number, car_make, car_model, int(car_price), car_colour, int(car_engine_capacity)) # Değerleri car değişkeninin içine kaydeder.

        result = car_management.add_car(car) # araç yönetimi modülü altında araç ekle fonksiyonuna car değişkenini ekleyip sonuç değişkenine sabitliyoruz.

        if result[0] == False: # Yine yukarıdaki sistem.
            print(result[1])
            __add_car(car)
        else:
            print("Car Successfully Added.")

def get_menu():
    while True: # Döngüyü almak için True döndürüyoruz.
        print(__menu) # Menü metni yazdırıyoruz.
        option = int(input("Car Management Menu : ")) # Menü yöentimi seçiyoruz.
        if option == 1: # 1. Seçenek Araç Ekleme seçilirse:
            print("Car Add is Working...")
            time.sleep(1)
            __add_car(None) # __add_car fonksiyonuna None tanımlıyoruz.
        elif option == 2: # 2. Seçenek Araç Listeleme seçilirse:
            os.system("cls")
            print("Cars are Listing...")
            time.sleep(1)
            car_list = car_management.list_car() # Car yönetimi modülü altında araç listele fonksiyonunu, araç listesi değişkenine eşitliyoruz.
            for car in car_list.items(): 
                print(car)
            print(input("Please Any Key to Continue..."))
        elif option == 3:
            os.system("cls")
            print("Car Delete is Working...")   
            time.sleep(1)                     
            car_list = car_management.list_car()
            for car in car_list.items(): 
                print(car)
            car_management.delete_car(int(input("Please Input Unique Id You Want to Delete Car : ")))
        elif option == 4:
            os.system("cls")
            print("Car Edit is Working...")   
            time.sleep(1)                     
            car_list = car_management.list_car()
            for car in car_list.items(): 
                print(car)
            car_management.edit_car(int(input("Please Input Unique Id You Want to Edit Car : ")))
        elif option == 5:
            menu_management.main_menu()
        else:
            print("Please Select Valid Choice!")
