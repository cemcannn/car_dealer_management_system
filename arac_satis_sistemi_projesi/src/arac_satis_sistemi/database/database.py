import sqlite3
import os

current_directory =  os.getcwd()
veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))

imlec = veritabanim.cursor()

imlec.execute("""CREATE TABLE IF NOT EXISTS araclar
                (Benzersiz_kod INTEGER NOT NULL, 
                Seri_no TEXT NOT NULL, 
                Marka TEXT NOT NULL, 
                Model TEXT NOT NULL, 
                Fiyat INTEGER NOT NULL, 
                Renk TEXT NOT NULL, 
                Silindir INTEGER NOT NULL,
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

imlec.execute("""CREATE TABLE IF NOT EXISTS personeller
                (Benzersiz_kod INTEGER NOT NULL, 
                Personel_TCKN TEXT NOT NULL, 
                Adi TEXT NOT NULL, 
                Soyadi TEXT NOT NULL, 
                Adres TEXT NOT NULL, 
                Telefon TEXT NOT NULL, 
                Gorev TEXT NOT NULL,                
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

imlec.execute("""CREATE TABLE IF NOT EXISTS musteriler
                (Benzersiz_kod INTEGER NOT NULL, 
                Musteri_TCKN TEXT NOT NULL, 
                Adi TEXT NOT NULL, 
                Soyadi TEXT NOT NULL, 
                Adres TEXT NOT NULL, 
                Telefon TEXT NOT NULL,
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

imlec.execute("""CREATE TABLE IF NOT EXISTS faturalar
                (Benzersiz_kod INTEGER NOT NULL, 
                Fatura_no TEXT NOT NULL, 
                Arac TEXT NOT NULL, 
                Musteri TEXT NOT NULL, 
                Personel TEXT NOT NULL, 
                Tutar INTEGER NOT NULL, 
                Tarih TEXT NOT NULL,                
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

veritabanim.commit()
veritabanim.close()
