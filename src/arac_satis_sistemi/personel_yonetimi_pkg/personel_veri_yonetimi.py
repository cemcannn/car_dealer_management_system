from .personel import Personel 
import sqlite3
import os

current_directory = os.getcwd()

def __open():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    return veritabanim

def __close(veritabanim):
    veritabanim.close()

def personel_ekle(personel:Personel): 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("INSERT INTO personeller VALUES (?,?,?,?,?,?,?)",(personel.benzersiz_kod,personel.tckn,personel.adi,personel.soyadi,personel.adres,personel.tel,personel.gorev))
    vt.commit()
    __close(vt)

def personel_sil(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("DELETE FROM personeller WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    vt.commit()
    __close(vt)

def personel_getir_benzersizkod(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM personeller WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    personel = imlec.fetchone()
    __close(vt)                             
    return personel

def personel_getir_tckn(tckn:int) -> Personel: 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM personeller WHERE Personel_TCKN = ?",(tckn,))
    personel = imlec.fetchone()
    __close(vt)     
    if tckn != None:
        return personel
    return None
              
def personel_listele() -> list():
    vt=__open()
    imlec = vt.cursor()
    sorgu = "SELECT * FROM personeller"
    imlec.execute(sorgu)
    personel_listesi = imlec.fetchall()
    __close(vt)
    return personel_listesi

def personel_duzenle(personel:Personel):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("UPDATE personeller SET Personel_TCKN = ?, Adi = ?, Soyadi = ?, Adres = ?, Telefon = ?, Gorev = ? WHERE Benzersiz_kod = ?",(personel.tckn,personel.adi,personel.soyadi,personel.adres,personel.tel,personel.gorev,personel.benzersiz_kod))
    vt.commit()
    __close(vt)
