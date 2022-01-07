from .fatura import Fatura
import sqlite3
import os

current_directory = os.getcwd()

def fatura_ekle(fatura:Fatura): 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("INSERT INTO faturalar VALUES (?,?,?,?,?,?,?)",(fatura.benzersiz_kod,fatura.no,fatura.arac,fatura.musteri,fatura.personel,fatura.tutar,fatura.tarih))
    veritabanim.commit()
    veritabanim.close()

def fatura_sil(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("DELETE FROM faturalar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    veritabanim.commit()
    veritabanim.close()

def fatura_getir_benzersizkod(benzersiz_kod:int):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM faturalar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    fatura = imlec.fetchone()
    veritabanim.close()                             
    return fatura

def fatura_getir_faturano(no:str) -> Fatura: 
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("SELECT * FROM faturalar WHERE Fatura_no = ?",(no,))
    fatura = imlec.fetchone()
    veritabanim.close()        
    if no != None:
        return fatura
    return None
              
def fatura_listele() -> list():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    sorgu = "SELECT * FROM faturalar"
    imlec.execute(sorgu)
    fatura_listesi = imlec.fetchall()
    return fatura_listesi

def fatura_duzenle(fatura:Fatura):
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    imlec = veritabanim.cursor()
    imlec.execute("UPDATE faturalar SET Fatura_no = ?, Arac = ?, Musteri = ?, Personel = ?, Tutar = ?, Tarih = ? WHERE Benzersiz_kod = ?",(fatura.no,fatura.arac,fatura.musteri,fatura.personel,fatura.tutar,fatura.tarih,fatura.benzersiz_kod))
    veritabanim.commit()
    veritabanim.close()
