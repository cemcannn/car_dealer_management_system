from .musteri import Musteri 
import sqlite3
import os

current_directory = os.getcwd()

def __open():
    veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))
    return veritabanim

def __close(veritabanim):
    veritabanim.close()

def musteri_ekle(musteri:Musteri): 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("INSERT INTO musteriler VALUES (?,?,?,?,?,?)",(musteri.benzersiz_kod,musteri.tckn,musteri.adi,musteri.soyadi,musteri.adres,musteri.tel))
    vt.commit()
    __close(vt)

def musteri_sil(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("DELETE FROM musteriler WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    vt.commit()
    __close(vt)

def musteri_getir_benzersizkod(benzersiz_kod:int):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM musteriler WHERE Benzersiz_kod = ?",(benzersiz_kod,))
    musteri = imlec.fetchone()
    __close(vt)                             
    return musteri

def musteri_getir_tckn(tckn:int) -> Musteri: 
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("SELECT * FROM musteriler WHERE Musteri_TCKN = ?",(tckn,))
    musteri = imlec.fetchone()
    __close(vt)        
    if tckn != None:
        return musteri
    return None
              
def musteri_listele() -> list():
    vt=__open()
    imlec = vt.cursor()
    sorgu = "SELECT * FROM musteriler"
    imlec.execute(sorgu)
    musteri_listesi = imlec.fetchall()
    __close(vt)
    return musteri_listesi

def musteri_duzenle(musteri:Musteri):
    vt=__open()
    imlec = vt.cursor()
    imlec.execute("UPDATE musteriler SET Musteri_TCKN = ?, Adi = ?, Soyadi = ?, Adres = ?, Telefon = ? WHERE Benzersiz_kod = ?",(musteri.tckn,musteri.adi,musteri.soyadi,musteri.adres,musteri.tel,musteri.benzersiz_kod))
    vt.commit()
    __close(vt)
