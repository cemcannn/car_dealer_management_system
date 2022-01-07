class Arac: 
    def __init__(self, benzersiz_kod: int, serino: str, marka: str, model: str, fiyat: int, renk: str, silindir: int):
        self.benzersiz_kod  = benzersiz_kod
        self.serino         = serino # pattern A000-0000
        self.marka          = marka
        self.model          = model
        self.fiyat          = fiyat
        self.renk           = renk 
        self.silindir       = silindir

    def __str__(self): 
        return f"Araç ID = {self.benzersiz_kod}, Araç Seri Numarası = {self.serino}, Araç Markası = {self.marka}, Araç Modeli = {self.model}, Araç Fiyatı = {self.fiyat}, Araç Silindir Sayısı = {self.silindir}"

