import menu_yonetimi
from fatura_yonetimi_pkg import fatura_veri_yonetimi as avy
from musteri_yonetimi_pkg import musteri_veri_yonetimi as mvy
from personel_yonetimi_pkg import personel_veri_yonetimi as pvy
from .fatura import Fatura
from . import fatura_yonetimi
import time
import os
from datetime import datetime

__menu_metni =("""
            ===========================
            Fatura Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Fatura Ekle
            (2) Fatura Listele
            (3) Fatura Sil
            (4) Fatura Düzenle
            (5) Ana Menüye Dön
            ===========================
            """)

def __fatura_ekle(fatura:Fatura):
    if fatura == None:
        fatura_benzersiz_kod            = None
        fatura_no                       = input("Lütfen Fatura Numarasını 'AAA2021000000' Pattern Örneğine göre Giriniz : ")
        os.system("cls")
        print(avy.fatura_listele())
        fatura_arac                     = avy.fatura_getir_benzersizkod(int(input("Fatura Benzersiz Kod Giriniz : ")))
        os.system("cls")
        print(mvy.musteri_listele())
        fatura_musteri                  = mvy.musteri_getir_benzersizkod(int(input("Fatura Benzersiz Kod Giriniz : ")))
        os.system("cls")
        print(pvy.personel_listele())
        fatura_personel                 = pvy.personel_getir_benzersizkod(int(input("Personel Benzersiz Kod Giriniz : ")))
        fatura_tutari                   = fatura_yonetimi.__vergi_hesapla(fatura_arac)
        moment                          = datetime.now()
        fatura_tarihi                   = datetime.strftime(moment, '%c')
        fatura = Fatura(fatura_benzersiz_kod, fatura_no, fatura_arac, fatura_musteri, fatura_personel, fatura_tutari, fatura_tarihi)

        sonuc = fatura_yonetimi.fatura_ekle(fatura)

        if sonuc[0] == False:
            print(sonuc[1])
            __fatura_ekle(fatura)
        else:
            print("Fatura Başarıyla Kaydedildi.") 
    
    else:
        print("Daha Önce Girdiğiniz Değeri Dabul Etmek için Enter Tuşuna Basınız.")
        fatura_no                       = input(f"Lütfen Fatura Numarasını 'AAA2021000000' Pattern Örneğine göre Giriniz({fatura.no}) : ")
        os.system("cls")
        print(avy.fatura_listele())
        fatura_arac                     = avy.fatura_getir_benzersizkod(int(input(f"Fatura Benzersiz Kod Giriniz ({fatura.arac}): ")))
        os.system("cls")        
        print(mvy.musteri_listele())
        fatura_musteri                  = mvy.musteri_getir_benzersizkod(int(input(f"Fatura Benzersiz Kod Giriniz ({fatura.musteri}): ")))
        os.system("cls")
        print(pvy.personel_listele())
        fatura_personel                 = pvy.personel_getir_benzersizkod(int(input(f"Personel Benzersiz Kod Giriniz ({fatura.personel}): ")))
        fatura_tutari                   = fatura_yonetimi.__vergi_hesapla(fatura_arac)
        moment                          = datetime.now()
        fatura_tarihi                   = datetime.strftime(moment, '%c')

        if fatura_no == "":
            fatura_no = fatura.no
        
        if fatura_arac == "":
            fatura_arac = fatura.arac

        if fatura_musteri == "":
            fatura_musteri = fatura.musteri
            
        if fatura_personel == "":
            fatura_personel = fatura.personel
        
        if fatura_tutari == "":
            fatura_tutari = fatura.tutar
        
        if fatura_tarihi == "":
            fatura_tarihi = fatura.tarih

        fatura = Fatura(fatura.benzersiz_kod, fatura_no, fatura_arac, fatura_musteri, fatura_personel, fatura_tutari, fatura_tarihi)

        sonuc = fatura_yonetimi.fatura_ekle(fatura)

        if sonuc[0] == False:
            print(sonuc[1])
            __fatura_ekle(fatura)
        else:
            print("Fatura Başarıyla Kaydedildi.") 

def __fatura_duzenle(benzersiz_kod):
    fatura = fatura_yonetimi.fatura_getir(benzersiz_kod)
    print(fatura)
    fatura_benzersiz_kod = fatura[0]
    fatura_no                       = input(f"Lütfen Fatura Numarasını 'AAA2021000000' Pattern Örneğine göre Giriniz({fatura[1]}) : ")
    os.system("cls")
    print(avy.fatura_listele())
    fatura_arac                     = avy.fatura_getir_benzersizkod(int(input(f"Fatura Benzersiz Kod Giriniz ({fatura[2]}): ")))
    os.system("cls")        
    print(mvy.musteri_listele())
    fatura_musteri                  = mvy.musteri_getir_benzersizkod(int(input(f"Fatura Benzersiz Kod Giriniz ({fatura[3]}): ")))
    os.system("cls")
    print(pvy.personel_listele())
    fatura_personel                 = pvy.personel_getir_benzersizkod(int(input(f"Personel Benzersiz Kod Giriniz ({fatura[4]}): ")))
    fatura_tutari                   = fatura_yonetimi.__vergi_hesapla(fatura_arac)
    moment                          = datetime.now()
    fatura_tarihi                   = datetime.strftime(moment, '%c')

    if fatura_no == "":
        fatura_no = fatura[1]
        
    if fatura_arac == "":
        fatura_arac = fatura[2]

    if fatura_musteri == "":
        fatura_musteri = fatura[3]
            
    if fatura_personel == "":
        fatura_personel = fatura[4]
        
    if fatura_tutari == "":
        fatura_tutari = fatura[5]
        
    if fatura_tarihi == "":
        fatura_tarihi = fatura[6]

    fatura = Fatura(fatura_benzersiz_kod, fatura_no, fatura_arac, fatura_musteri, fatura_personel, fatura_tutari, fatura_tarihi)

    sonuc = fatura_yonetimi.fatura_duzenle(fatura)

    if sonuc[0] == False:
        print(sonuc[1])
        __fatura_duzenle(fatura)
    else:
        print("Fatura Başarıyla Kaydedildi.") 

def menu_getir():
    while True: # Döngüyü almak için True döndürüyoruz.
        print(__menu_metni) # Menü metni yazdırıyoruz.
        secenek = int(input("Arac Yonetimi Menü Seçiminizi Yapınız: ")) # Menü yöentimi seçiyoruz.
        if secenek == 1: # 1. Seçenek Fatura Ekleme seçilirse:
            print("Fatura Ekleme Çalışıyor...")
            time.sleep(1)
            __fatura_ekle(None) # __fatura_ekle fonksiyonuna None tanımlıyoruz.
        elif secenek == 2: # 2. Seçenek Fatura Listeleme seçilirse:
            os.system("cls")
            print("Faturalar listeleniyor...")
            time.sleep(1)
            fatura_listesi = fatura_yonetimi.fatura_listele() # Arac yönetimi modülü altında araç listele fonksiyonunu, araç listesi değişkenine eşitliyoruz.
            for fatura in fatura_listesi: 
                print(fatura)
            print(input("Devam Etmek için Bir Tuşa Basınız..."))
        elif secenek == 3:
            os.system("cls")
            print("Fatura Silme Çalışıyor...")   
            time.sleep(1)                     
            fatura_listesi = fatura_yonetimi.fatura_listele()
            for fatura in fatura_listesi: 
                print(fatura)
            fatura_yonetimi.fatura_sil(input("Lütfen Silmek İstediğiniz Aracın Benzersiz Kodunu Giriniz : "))
        elif secenek == 4:
            os.system("cls")
            print("Fatura Düzenleme Çalışıyor...")   
            time.sleep(1)                     
            fatura_listesi = fatura_yonetimi.fatura_listele()
            for fatura in fatura_listesi: 
                print(fatura)
            __fatura_duzenle(input("Lütfen Düzenlemek İstediğiniz Faturanın Benzersiz Kodunu Giriniz : "))
        elif secenek == 5:
            menu_yonetimi.ana_menu_getir()
        else:
            print("Lütfen Doğru Seçeneği Seçiniz!")