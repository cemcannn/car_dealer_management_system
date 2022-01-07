from arac_yonetimi_pkg import arac
from musteri_yonetimi_pkg import musteri
from personel_yonetimi_pkg import personel

class Fatura:
    def __init__(self,benzersiz_kod: int, no:complex, arac: arac.Arac, musteri: musteri.Musteri, personel: personel.Personel, tutar:int, tarih:int):
        self.benzersiz_kod  = benzersiz_kod
        self.no             = no    
        self.arac           = arac
        self.musteri        = musteri
        self.personel       = personel
        self.tutar          = tutar
        self.tarih          = tarih

    def __str__(self): 
        return f"ID = {self.benzersiz_kod}, Fatura No = {self.no}, Araç = {self.arac}, Müşteri = {self.musteri}, Personel = {self.personel}, Fatura Tutarı = {self.tutar}, Fatura Tarihi = {self.tarih} "
