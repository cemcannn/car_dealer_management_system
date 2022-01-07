from .musteri import Musteri 
import sqlite3
import os

current_directory = os.getcwd()

def musteri_ekle(musteri:Musteri): 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("INSERT INTO musteriler VALUES (?,?,?,?,?,?)",(musteri.benzersiz_kod,musteri.tckn,musteri.adi,musteri.soyadi,musteri.adres,musteri.tel))
    veritabanim.commit()
    veritabanim.close()

def musteri_sil(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("DELETE FROM musteriler WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    veritabanim.commit()
    veritabanim.close()

def musteri_getir_benzersizkod(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM musteriler WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    musteri = imlec.fetchone()
    veritabanim.close()                             
    return musteri

def musteri_getir_tckn(tckn:int) -> Musteri: 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM musteriler WHERE Musteri_TCKN = ?",(tckn,))
    musteri = imlec.fetchone()
    veritabanim.close()        
    if tckn != None:
        return musteri
    return None
              
def musteri_listele() -> list():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    sorgu = "SELECT * FROM musteriler"
    imlec.execute(sorgu)
    musteri_listesi = imlec.fetchall()
    return musteri_listesi

def musteri_duzenle(musteri:Musteri):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("UPDATE musteriler SET Musteri_TCKN = ?, Adi = ?, Soyadi = ?, Adres = ?, Telefon = ? WHERE Benzersiz_kod = ?",(musteri.tckn,musteri.adi,musteri.soyadi,musteri.adres,musteri.tel,musteri.benzersiz_kod))
    veritabanim.commit()
    veritabanim.close()
    
