from arac_yonetimi_pkg import arac_menu_yonetimi 
from musteri_yonetimi_pkg import musteri_menu_yonetimi 
from personel_yonetimi_pkg import personel_menu_yonetimi 
from fatura_yonetimi_pkg import fatura_menu_yonetimi 
from tkinter import *


menu_metni = """ Seçenekler:
                [1] Araç Yönetimi İçin 
                [2] Müşteri Yönetimi İçin 
                [3] Personel Yönetimi İçin 
                [4] Fatura Yönetimi İçin 
                [5] Çıkmak İçin 5"""


def ana_menu_getir(): 
    while True:
        print(menu_metni)
        secenek = int(input("menu seçinizi yapınız: "))
        if secenek == 1:
            arac_menu_yonetimi.menu_getir()
        elif secenek == 2:
            musteri_menu_yonetimi.menu_getir()
        elif secenek == 3:
            personel_menu_yonetimi.menu_getir()
        elif secenek == 4:
            fatura_menu_yonetimi.menu_getir()
        elif secenek == 5:
            quit()
        else:
            print("yanlış seçim yaptınız")

# pencere = Tk()

# hesap_alani = Entry(pencere)
# hesap_alani.insert(0,"")
# hesap_alani.grid(row=0, columnspan=5)

# menu_01 = Button(pencere, text="Araç Yönetimi Menüsü",command = arac_menu_yonetimi.menu_getir())
# menu_01.grid(row=1,columnspan=5)
# menu_02 = Button(pencere, text="Müşteri Yönetimi Menüsü",command = lambda: musteri_menu_yonetimi.menu_getir())
# menu_02.grid(row=2,columnspan=5)
# menu_03 = Button(pencere, text="Personel Yönetimi Menüsü",command = lambda: personel_menu_yonetimi.menu_getir())
# menu_03.grid(row=3,columnspan=5)
# menu_04 = Button(pencere, text="Fatura Yönetimi Menüsü",command = lambda: fatura_menu_yonetimi.menu_getir())
# menu_04.grid(row=4,columnspan=5)
# menu_05 = Button(pencere, text="Çıkış",command = lambda: quit())
# menu_05.grid(row=5,columnspan=5)


# pencere.mainloop()