# Sıcak - Soğuk Tahmin Oyunu

import random
import os
os.system('clear') # Consolu temizliyor. MacOS için 'clear' , Windows için 'cls'

def tahminOyunu ():
    #sayi = 99
    sayi = random.randint(0, 100) # 0-100 arasında random bir integer değer üretiliyor.
    hak = 5
    print("Aklımda 0 - 100 arasında bir sayı tuttum...")
    while True:
        tahminSayi = int(input(f"Aklımdaki sayıyı tahmin ediniz (Tahmin hakkınız : {hak}) : "))
        hak -= 1
        if tahminSayi == sayi:
            print(f"Tebrikler, aklımdaki {sayi} sayısını doğru bildin.")
            break
        elif hak == 0:
            print(f"Kalan hakkın {hak}. Hakların bitmeden aklımdaki sayıyı bilemedin..!")
            break
        elif tahminSayi < sayi and (sayi - tahminSayi <= 10):
            print("Sıcak.! Yükseltin..")
        elif tahminSayi > sayi and (tahminSayi - sayi <= 10):
            print("Sıcak.! Azaltın..")
        elif tahminSayi < sayi and (sayi - tahminSayi > 10):
            print("Soğuk.! Yükseltin..")
        elif tahminSayi > sayi and (tahminSayi - sayi > 10):
            print("Soğuk.! Azaltın..")
tahminOyunu()