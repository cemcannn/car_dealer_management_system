import menu_yonetimi
from .personel import Personel
from . import personel_yonetimi
import os
import time

__menu_metni =("""
            ===========================
            Personel Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Personel Ekle
            (2) Personel Listele
            (3) Personel Sil
            (4) Personel Düzenle
            (5) Ana Menüye Dön
            ===========================
            """)

def __personel_ekle(personel:Personel):
    if personel == None:
        personel_benzersiz_kod   = None
        personel_tckn            = input("Lütfen 11 Haneli Personel TCKN Giriniz : ")
        personel_adi             = input("Personel Adını Giriniz : ")
        personel_soyadi          = input("Personel Soyadını Giriniz : ")
        personel_adresi          = input("Personel Adresini Giriniz : ")
        personel_telefonu        = input("Personel Telefonunu Başında '0' Olmadan Giriniz : ")
        personel_gorevi          = input("Personel Görevini Giriniz : ")
        personel = Personel(personel_benzersiz_kod, personel_tckn, personel_adi, personel_soyadi, personel_adresi, personel_telefonu, personel_gorevi)

        sonuc = personel_yonetimi.personel_ekle(personel)

        if sonuc[0] == False:
            print(sonuc[1])
            __personel_ekle(personel)
        else:
            print("Personel Başarıyla Kaydedildi.") 
    
    else:
        print("Daha Önce Girdiğiniz Değeri Kabul Etmek için Enter Tuşuna Basınız.")
        personel_tckn        = input(f"Lütfen 11 Haneli Personel TCKN Giriniz ({personel.tckn}) : ")
        personel_adi         = input(f"Personel Adını Giriniz ({personel.adi}): ")
        personel_soyadi      = input(f"Personel Soyadını Giriniz ({personel.soyadi}) : ")
        personel_adresi      = input(f"Personel Adresini Giriniz ({personel.adres}) : ")
        personel_telefonu    = input(f"Personel Telefonunu Başında '0' Olmadan Giriniz ({personel.tel}) : ")
        personel_gorevi      = input(f"Personel Görevini Giriniz ({personel.gorev}) : ")

        if personel_tckn == "":
            personel_tckn = personel.tckn
        
        if personel_adi == "":
            personel_adi = personel.adi

        if personel_soyadi == "":
            personel_soyadi = personel.soyadi
        
        if personel_adresi == "":
            personel_adresi = personel.adres
        
        if personel_telefonu == "":
            personel_telefonu = personel.tel

        if personel_gorevi == "":
            personel_gorevi = personel.gorev

        personel = Personel(personel.benzersiz_kod, personel_tckn, personel_adi, personel_soyadi, personel_adresi, personel_telefonu, personel_gorevi)

        sonuc = personel_yonetimi.personel_ekle(personel)

        if sonuc[0] == False:
            print(sonuc[1])
            __personel_ekle(personel)
        else:
            print("Personel Başarıyla Kaydedildi.") 

def __personel_duzenle(benzersiz_kod):
    personel = personel_yonetimi.personel_getir(benzersiz_kod)
    print(personel)
    personel_benzersiz_kod = personel[0]
    personel_tckn        = input(f"Lütfen 11 Haneli Personel TCKN Giriniz ({personel[1]}) : ")
    personel_adi         = input(f"Personel Adını Giriniz ({personel[2]}): ")
    personel_soyadi      = input(f"Personel Soyadını Giriniz ({personel[3]}) : ")
    personel_adresi      = input(f"Personel Adresini Giriniz ({personel[4]}) : ")
    personel_telefonu    = input(f"Personel Telefonunu Başında '0' Olmadan Giriniz ({personel[5]}) : ")
    personel_gorevi      = input(f"Personel Görevini Giriniz ({personel[6]}) : ")

    if personel_tckn == "":
        personel_tckn = personel[1]
        
    if personel_adi == "":
        personel_adi = personel[2]

    if personel_soyadi == "":
        personel_soyadi = personel[3]
        
    if personel_adresi == "":
        personel_adresi = personel[4]
        
    if personel_telefonu == "":
        personel_telefonu = personel[5]

    if personel_gorevi == "":
        personel_gorevi = personel[6]

    personel = Personel(personel_benzersiz_kod, personel_tckn, personel_adi, personel_soyadi, personel_adresi, personel_telefonu, personel_gorevi)

    sonuc = personel_yonetimi.personel_duzenle(personel)

    if sonuc[0] == False:
        print(sonuc[1])
        __personel_duzenle(personel)
    else:
        print("Personel Başarıyla Kaydedildi.") 

def menu_getir(): 
    while True:
        print(__menu_metni)
        secenek = int(input("Personel Yönetimi Menü Seçiminizi Yapınız: "))
        if secenek == 1:
            print("Personel Ekleme Çalışıyor")
            time.sleep(1)
            __personel_ekle(None)
        elif secenek == 2:
            os.system("cls")
            print("Personeller listeleniyor...")
            time.sleep(1)
            personel_listesi = personel_yonetimi.personel_listele()
            for personel in personel_listesi:
                print(personel)
            print(input("Devam Etmek için Bir Tuşa Basınız..."))                
        elif secenek == 3:
            os.system("cls")
            print("Personel Silme Çalışıyor...")   
            time.sleep(1)               
            personel_listesi = personel_yonetimi.personel_listele()
            for personel in personel_listesi:
                print(personel)
            personel_yonetimi.personel_sil(input("Lütfen Silmek İstediğiniz Personelin Benzersiz Kodunu Giriniz : "))
        elif secenek == 4:
            os.system("cls")
            print("Personel Düzenleme Çalışıyor...")   
            time.sleep(1)                     
            personel_listesi = personel_yonetimi.personel_listele()
            for personel in personel_listesi: 
                print(personel)
            __personel_duzenle(input("Lütfen Düzenlemek İstediğiniz Personelin Benzersiz Kodunu Giriniz :"))
        elif secenek == 5:
            menu_yonetimi.ana_menu_getir()
        else:
            print("Lütfen Doğru Seçeneği Seçiniz!")            
            