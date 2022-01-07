from .personel import Personel
from . import personel_veri_yonetimi
import re

def __personel_dogrula(personel: Personel) -> (bool,str):
    pattern     = "[1-9]{1}[0-9]{10}"
    sonuc       = re.search(pattern, personel.tckn)
    pattern2    = "[1-9]{1}[0-9]{9}"
    sonuc2      = re.search(pattern2, personel.tel)
    if sonuc == None:
        return (False, "TCKN Patterne Uygun Olmalıdır!")
    
    if personel_veri_yonetimi.personel_getir_tckn(personel.tckn) != None:
        return (False, f"{personel.tckn} Personel TCKN'sı Daha Önce Sisteme Kaydedilmiş!")
    
    if sonuc2 == None:
        return (False, "Telefon Numarası Patterne Uygun Olmalıdır!")

    return (True, "Personel Doğrulandı")

def personel_ekle(personel:Personel) -> (bool,str):
    try:
        dogrulama_sonucu = __personel_dogrula(personel)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu
        
        personel_veri_yonetimi.personel_ekle(personel)

        return (True, "Kayıt Başarıyla Yapılmıştır.")
    except Exception as ex:
        return (False, "Hata Meydana Geldi : " + ex.__str__())        

def personel_listele() -> {Personel}:
    return personel_veri_yonetimi.personel_listele()

def personel_sil(benzersiz_kod: int) -> bool:
    try:
        personel_veri_yonetimi.personel_sil(benzersiz_kod)
    except:
        return False

def personel_duzenle(personel:Personel) -> (bool,str):
    try:
        dogrulama_sonucu = __personel_dogrula(personel)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu

        personel_veri_yonetimi.personel_duzenle(personel)
        return (True, "Kayıt Başarıyla Yapılmıştır.")
        
    except Exception as ex:
        return (False, "Hata Meydana Geldi : " + ex.__str__())
    
def personel_getir(benzersiz_kod: int) -> Personel:
    try:
        return personel_veri_yonetimi.personel_getir_benzersizkod(benzersiz_kod)
    except:
        return Personel()
