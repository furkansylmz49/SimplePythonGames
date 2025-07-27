from random import choice
from random import randint

def TasKağıtMakas():
    KullanıcıSkoru = 0
    BilgisyarSkoru = 0

    while not(KullanıcıSkoru >= 3 or BilgisyarSkoru >= 3):
        BilgisayarSeçimi = choice(["Taş","Kağıt","Makas"]).lower()
        KullanıcıSeçimi = input("Taş mı Kağıt mı Makas mı? ").lower()

        print(f"Bilgisayarın Seçimi: {BilgisayarSeçimi}")

        if KullanıcıSeçimi == BilgisayarSeçimi:
            print("Berabere")
        elif KullanıcıSeçimi == "kağıt" and BilgisayarSeçimi == "taş":
            print("Tebrikler. Kazandınız")
            KullanıcıSkoru += 1
            print(f"Durum: Siz= {KullanıcıSkoru} Bilgisayar= {BilgisyarSkoru}")
        elif KullanıcıSeçimi == "taş" and BilgisayarSeçimi == "makas":
            print("Tebrikler. Kazandınız")
            KullanıcıSkoru += 1
            print(f"Durum: Siz= {KullanıcıSkoru} Bilgisayar= {BilgisyarSkoru}")
        elif KullanıcıSeçimi == "makas" and BilgisayarSeçimi == "kağıt":
            print("Tebrikler. Kazandınız")
            KullanıcıSkoru += 1
            print(f"Durum: Siz= {KullanıcıSkoru} Bilgisayar= {BilgisyarSkoru}")
        else:
            print("Kaybettiniz. Bilgisyar Kazandı")
            BilgisyarSkoru += 1
            print(f"Durum: Siz= {KullanıcıSkoru} Bilgisayar= {BilgisyarSkoru}")

    if KullanıcıSkoru >= 3:
        print("Oyunu siz kazandınız tebrikler")
    else:
        print("Oyunu kaybettiniz. Bilgisayar kazandı")


def SayıTahminOyunu():
    BilgisayarSayısı = randint(0,100)
    DenemeSayısı = 1
    KullanıcıTahmini = None


    while not(KullanıcıTahmini == BilgisayarSayısı):
        KullanıcıTahmini = int(input("Lütfen Tahmininizi Giriniz."))
        print(f"{DenemeSayısı}. Denemeniz")

        if KullanıcıTahmini > BilgisayarSayısı:
            print("Azaltın")
            DenemeSayısı += 1
        elif KullanıcıTahmini < BilgisayarSayısı:
            print("Arttırın")
            DenemeSayısı += 1
        else:
            print(f"Tebrikler. {DenemeSayısı}. deneme de buldunuz.")



print("Zeka Küpü - Mini Oyunlar")
print("1 -> Taş Kağıt Makas")
print("2 -> Sayı Tahmin Oyunu")
print("3 -> Kelime Karıştırmaca")
print("4 -> Çıkış")
OyunSeçimi = int(input("Seçiminiz: "))


if OyunSeçimi == 1:
    print("Taş Kağıt Makas Oyununa Hoş Geldiniz")
    TasKağıtMakas()
elif OyunSeçimi == 2:
    print("Sayı Tahmin Oyununa Hoş Geldiniz")
    SayıTahminOyunu()