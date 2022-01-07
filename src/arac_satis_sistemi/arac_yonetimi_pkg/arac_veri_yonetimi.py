from .arac import Arac 
import sqlite3
import os

current_directory = os.getcwd()

def arac_ekle(arac:Arac): 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("INSERT INTO araclar VALUES (?,?,?,?,?,?,?)",(arac.benzersiz_kod,arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir))
    veritabanim.commit()
    veritabanim.close()

def arac_sil(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("DELETE FROM araclar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    veritabanim.commit()
    veritabanim.close()

def arac_getir_benzersizkod(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM araclar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    arac = imlec.fetchone()
    veritabanim.close()                             
    return arac

def arac_getir_serino(serino:str) -> Arac: 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM araclar WHERE Seri_no = ?",(serino,))
    arac = imlec.fetchone()
    veritabanim.close()        
    if serino != None:
        return arac
    return None
              
def arac_listele() -> list():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    sorgu = "SELECT * FROM araclar"
    imlec.execute(sorgu)
    arac_listesi = imlec.fetchall()
    return arac_listesi

def arac_duzenle(arac:Arac):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("UPDATE araclar SET Seri_no = ?, Marka = ?, Model = ?, Fiyat = ?, Renk = ?, Silindir = ? WHERE Benzersiz_kod = ?",(arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir,arac.benzersiz_kod))
    veritabanim.commit()
    veritabanim.close()



