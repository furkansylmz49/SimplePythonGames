from random import choice
from random import randint
from random import shuffle

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


def KelimeKarıştırmaca(ZorlukSeviyesi):
    KelimeDenemeSayısı = 0

    if ZorlukSeviyesi == 5:
        easy_words = ["apple", "grape", "lemon", "table", "chair","piano", "heart", "bread", "smile", "house","plant", "stone", "water", "light", "river"]
        SeçilenKelime = choice(easy_words)
    elif ZorlukSeviyesi == 6:
        medium_words = ["banana", "window", "marker", "pencil", "rocket","planet", "father", "mother", "friend", "screen","summer", "winter", "forest", "laptop", "galaxy"]
        SeçilenKelime = choice(medium_words)
    elif ZorlukSeviyesi == 7:
        hard_words = ["freedom", "justice", "respect", "courage", "honesty","backpack", "picture", "teacher", "notebook", "holiday","library", "deserts", "animals", "emotion", "support"]
        SeçilenKelime = choice(medium_words)

    HarfList = list(SeçilenKelime)
    shuffle(HarfList)
    KarışıkKelime = ''.join(HarfList)

    print(f"Scrambled word: {KarışıkKelime}")

    while not(KelimeDenemeSayısı == 3):
        KelimeDenemeSayısı +=1
        YourGuess = input("Your guess:")

        if SeçilenKelime == YourGuess:
            print(f"{KelimeDenemeSayısı}. Denemede Buldunuz. Tebrikler")
            break
        else:
            print(f"Incorrect. Please tr again ({3-KelimeDenemeSayısı} Hakkınız kaldı)")
    else:
        print("Başarısız oldunuz. üzgünüm")
        





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
elif OyunSeçimi == 3:
    print("Kelime Karıştırıcya HoşGeldiniz")
    ZorlukSeviyesi = int(input("Lütfen Zorluk Seviyesini Giriniz"))
    KelimeKarıştırmaca(ZorlukSeviyesi)