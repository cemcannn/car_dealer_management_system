from .personel import Personel 
import sqlite3
import os

current_directory = os.getcwd()

def personel_ekle(personel:Personel): 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("INSERT INTO personeller VALUES (?,?,?,?,?,?,?)",(personel.benzersiz_kod,personel.tckn,personel.adi,personel.soyadi,personel.adres,personel.tel,personel.gorev))
    veritabanim.commit()
    veritabanim.close()

def personel_sil(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("DELETE FROM personeller WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    veritabanim.commit()
    veritabanim.close()

def personel_getir_benzersizkod(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM personeller WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    personel = imlec.fetchone()
    veritabanim.close()                             
    return personel

def personel_getir_tckn(tckn:int) -> Personel: 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM personeller WHERE Personel_TCKN = ?",(tckn,))
    personel = imlec.fetchone()
    veritabanim.close()        
    if tckn != None:
        return personel
    return None
              
def personel_listele() -> list():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    sorgu = "SELECT * FROM personeller"
    imlec.execute(sorgu)
    personel_listesi = imlec.fetchall()
    return personel_listesi

def personel_duzenle(personel:Personel):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("UPDATE personeller SET Personel_TCKN = ?, Adi = ?, Soyadi = ?, Adres = ?, Telefon = ?, Gorev = ? WHERE Benzersiz_kod = ?",(personel.tckn,personel.adi,personel.soyadi,personel.adres,personel.tel,personel.gorev,personel.benzersiz_kod))
    veritabanim.commit()
    veritabanim.close()
