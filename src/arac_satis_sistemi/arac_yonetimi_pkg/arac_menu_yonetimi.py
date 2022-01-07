from .arac import Arac
from . import arac_yonetimi
import menu_yonetimi
import os
import time
from tkinter import *

__menu_metni =("""
            ===========================
            Araç Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Araç Ekle
            (2) Araç Listele
            (3) Araç Sil
            (4) Araç Düzenle
            (5) Ana Menüye Dön
            ===========================
            """)

def __arac_ekle(arac:Arac):
    if arac==None:
        arac_benzersiz_kod  = None
        arac_serino         = input("Lütfen Araç Seri Numarasını 'A000-0000' Pattern Örneğine göre Giriniz : ")
        arac_marka          = input("Lütfen Araç Markasını Giriniz : ")
        arac_model          = input("Lütfen Araç Modelini Giriniz : ")
        arac_fiyat          = input("Lütfen Araç Fiyatını Giriniz : ")
        arac_renk           = input("Lütfen Araç Rengini Giriniz : ")
        arac_silindir       = input("Lütfen Araç Silindir Sayısını Giriniz : ")
        arac = Arac(arac_benzersiz_kod, arac_serino, arac_marka, arac_model, int(arac_fiyat), arac_renk, int(arac_silindir))

        sonuc = arac_yonetimi.arac_ekle(arac)

        if sonuc[0] == False:
            print(sonuc[1])
            __arac_ekle(arac)
        else:
            print("Araç Başarıyla Kaydedildi.")

    else:
        print("Daha Önce Girdiğiniz Değeri Kabul Etmek için Enter Tuşuna Basınız.")
        arac_serino     = input(f"Lütfen Araç Seri Numarasını 'A000-0000' Pattern Örneğine göre Giriniz ({arac.serino}):") # Eğer araç seri nosu araç paternine uymuyorsa bizden tekrar seri no istiyor ve araç seri no yazdırıyor.
        arac_marka      = input(f"Lütfen Araç Markasını Giriniz ({arac.marka}): ")
        arac_model      = input(f"Lütfen Araç Modelini Giriniz ({arac.model}): ")
        arac_fiyat      = input(f"Lütfen Araç Fiyatını Giriniz ({arac.fiyat}): ")
        arac_renk       = input(f"Lütfen Araç Rengini Giriniz ({arac.renk}): ")
        arac_silindir   = input(f"Lütfen Araç Silindir Sayısını Giriniz ({arac.silindir}): ")

        if arac_serino == "":
            arac_serino = arac.serino

        if arac_marka == "":
            arac_marka = arac.marka

        if arac_model == "":
            arac_model = arac.model

        if arac_fiyat == "":
            arac_fiyat = arac.fiyat

        if arac_renk == "":
            arac_renk = arac.renk

        if arac_silindir == "":
            arac_silindir = arac.silindir

        arac = Arac(arac.benzersiz_kod, arac_serino, arac_marka, arac_model, int(arac_fiyat), arac_renk, int(arac_silindir))

        sonuc = arac_yonetimi.arac_ekle(arac)

        if sonuc[0] == False:
            print(sonuc[1])
            __arac_ekle(arac)
        else:
            print("Araç Başarıyla Kaydedildi.")

def __arac_duzenle(benzersiz_kod):
    arac = arac_yonetimi.arac_getir(benzersiz_kod)
    print(arac)
    arac_benzersiz_kod = arac[0]
    arac_serino     = input(f"Lütfen Araç Seri Numarasını 'A000-0000' Pattern Örneğine göre Giriniz ({arac[1]}):")
    arac_marka      = input(f"Lütfen Araç Markasını Giriniz ({arac[2]}): ")
    arac_model      = input(f"Lütfen Araç Modelini Giriniz ({arac[3]}): ")
    arac_fiyat      = input(f"Lütfen Araç Fiyatını Giriniz ({arac[4]}): ")
    arac_renk       = input(f"Lütfen Araç Rengini Giriniz ({arac[5]}): ")
    arac_silindir   = input(f"Lütfen Araç Silindir Sayısını Giriniz ({arac[6]}): ")

    if arac_serino == "":
        arac_serino = arac[1]

    if arac_marka == "":
        arac_marka = arac[2]

    if arac_model == "":
        arac_model = arac[3]

    if arac_fiyat == "":
        arac_fiyat = arac[4]

    if arac_renk == "":
        arac_renk = arac[5]

    if arac_silindir == "":
        arac_silindir = arac[6]

    arac = Arac(arac_benzersiz_kod, arac_serino, arac_marka, arac_model, int(arac_fiyat), arac_renk, int(arac_silindir))

    sonuc = arac_yonetimi.arac_duzenle(arac)

    if sonuc[0] == False:
        print(sonuc[1])
        __arac_duzenle(arac)
    else:
        print("Araç Başarıyla Kaydedildi.")

def menu_getir():
    while True:
        print(__menu_metni)
        secenek = int(input("Arac Yonetimi Menü Seçiminizi Yapınız: "))
        if secenek == 1:
            print("Araç Ekleme Çalışıyor...")
            time.sleep(1)
            __arac_ekle(None)
        elif secenek == 2:
            os.system("cls")
            print("Araçlar listeleniyor...")
            time.sleep(1)
            arac_listesi = arac_yonetimi.arac_listele()
            for arac in arac_listesi:
                print(arac)
            print(input("Devam Etmek için Bir Tuşa Basınız..."))
        elif secenek == 3:
            os.system("cls")
            print("Araç Silme Çalışıyor...")
            time.sleep(1)
            arac_listesi = arac_yonetimi.arac_listele()
            for arac in arac_listesi:
                print(arac)
            arac_yonetimi.arac_sil(input("Lütfen Silmek İstediğiniz Aracın Benzersiz Kodunu Giriniz : "))
        elif secenek == 4:
            os.system("cls")
            print("Araç Düzenleme Çalışıyor...")
            time.sleep(1)
            arac_listesi = arac_yonetimi.arac_listele()
            for arac in arac_listesi:
                print(arac)
            __arac_duzenle(input("Lütfen Düzenlemek İstediğiniz Aracın Benzersiz Kodunu Giriniz : "))
        elif secenek == 5:
            menu_yonetimi.ana_menu_getir()
        else:
            print("Lütfen Doğru Seçeneği Seçiniz!")

# pencere = Tk()

# hesap_alani = Entry(pencere)
# hesap_alani.insert(0,"")
# hesap_alani.grid(row=0, columnspan=5)

# menu_01 = Button(pencere, text="Araç Ekle",command = lambda: __arac_ekle(None))
# menu_01.grid(row=1,columnspan=5)
# menu_02 = Button(pencere, text="Araç Listele",command = lambda: arac_yonetimi.arac_listele())
# menu_02.grid(row=2,columnspan=5)
# menu_03 = Button(pencere, text="Araç Sil",command = lambda: arac_yonetimi.arac_sil(input("Lütfen Silmek İstediğiniz Aracın Benzersiz Kodunu Giriniz : ")))
# menu_03.grid(row=3,columnspan=5)
# menu_04 = Button(pencere, text="Araç Düzenle",command = lambda: __arac_duzenle(input("Lütfen Düzenlemek İstediğiniz Aracın Benzersiz Kodunu Giriniz : ")))
# menu_04.grid(row=4,columnspan=5)
# menu_05 = Button(pencere, text="Ana Menüye Dön",command = lambda: menu_yonetimi.ana_menu_getir())
# menu_05.grid(row=5,columnspan=5)

# pencere.mainloop()