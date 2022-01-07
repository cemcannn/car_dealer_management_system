class Musteri:
    def __init__(self,benzersiz_kod: int, tckn:int,adi:str,soyadi:str,adres:complex,tel:int):
        self.benzersiz_kod  = benzersiz_kod
        self.tckn           = tckn # Pattern: must be 11 character and integer
        self.adi            = adi
        self.soyadi         = soyadi
        self.adres          = adres
        self.tel            = tel

    def __str__(self): 
        return f"ID = {self.benzersiz_kod}, TCKN = {self.tckn}, Ad = {self.adi}, Soyad = {self.soyadi}, Adres = {self.adres}, Telefon = {self.tel} "
