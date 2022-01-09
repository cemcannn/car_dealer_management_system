from .arac import Arac 
import sqlite3
import os

current_directory = os.getcwd()

def __open():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    return veritabanim

def __close(veritabanim):
    veritabanim.close()

def arac_ekle(arac:Arac): 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("INSERT INTO araclar VALUES (?,?,?,?,?,?,?)",(arac.benzersiz_kod,arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir))
    vt.commit()
    __close(vt)

def arac_sil(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("DELETE FROM araclar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    vt.commit()
    __close(vt)

def arac_getir_benzersizkod(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM araclar WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    arac = imlec.fetchone()
    __close(vt)                           
    return arac

def arac_getir_serino(serino:str) -> Arac: 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM araclar WHERE Seri_no = ?",(serino,))
    arac = imlec.fetchone()
    __close(vt)      
    if serino != None:
        return arac
    return None
              
def arac_listele() -> list():
    vt=__open()
    imlec = vt.cursor()
    sorgu = "SELECT * FROM araclar"
    imlec.execute(sorgu)
    arac_listesi = imlec.fetchall()
    __close(vt)
    return arac_listesi

def arac_duzenle(arac:Arac):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("UPDATE araclar SET Seri_no = ?, Marka = ?, Model = ?, Fiyat = ?, Renk = ?, Silindir = ? WHERE Benzersiz_kod = ?",(arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir,arac.benzersiz_kod))
    vt.commit()
    __close(vt)



