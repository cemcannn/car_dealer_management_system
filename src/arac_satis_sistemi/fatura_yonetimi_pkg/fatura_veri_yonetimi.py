from .fatura import Fatura
import sqlite3
import os

current_directory = os.getcwd()

def __open():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    return veritabanim

def __close(veritabanim):
    veritabanim.close()

def fatura_ekle(fatura:Fatura): 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("INSERT INTO faturalar VALUES (?,?,?,?,?,?,?)",(fatura.benzersiz_kod,fatura.no,fatura.arac,fatura.musteri,fatura.personel,fatura.tutar,fatura.tarih))
    vt.commit()
    __close(vt)

def fatura_sil(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("DELETE FROM faturalar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    vt.commit()
    __close(vt)

def fatura_getir_benzersizkod(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM faturalar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    fatura = imlec.fetchone()
    __close(vt)                             
    return fatura

def fatura_getir_faturano(no:str) -> Fatura: 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM faturalar WHERE Fatura_no = ?",(no,))
    fatura = imlec.fetchone()
    __close(vt)        
    if no != None:
        return fatura
    return None
              
def fatura_listele() -> list():
    vt=__open()
    imlec = vt.cursor()
    sorgu = "SELECT * FROM faturalar"
    imlec.execute(sorgu)
    fatura_listesi = imlec.fetchall()
    __close(vt)
    return fatura_listesi

def fatura_duzenle(fatura:Fatura):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("UPDATE faturalar SET Fatura_no = ?, Arac = ?, Musteri = ?, Personel = ?, Tutar = ?, Tarih = ? WHERE Benzersiz_kod = ?",(fatura.no,fatura.arac,fatura.musteri,fatura.personel,fatura.tutar,fatura.tarih,fatura.benzersiz_kod))
    vt.commit()
    __close(vt)