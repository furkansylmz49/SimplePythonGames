from random import choice
from random import randint
from random import shuffle

def TasKağıtMakas():
    KullanıcıSkoru = 0
    BilgisyarSkoru = 0

    while not(KullanıcıSkoru >= 3 or BilgisyarSkoru >= 3):
        BilgisayarSeçimi = choice(["Taş","Kağıt","Makas"]).lower()
        
        while True:
            KullanıcıSeçimi = input("Taş mı Kağıt mı Makas mı? (Oyundan Çıkmak İçin 0' Basınız)").lower()

            geçerli_seçimler = ["taş", "kağıt", "makas", "0"]
            if KullanıcıSeçimi in geçerli_seçimler:
                break
            else:
                print("Geçersiz girdi, tekrar deneyiniz.")


        if KullanıcıSeçimi == "0":
            break

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
    BilgisayarSayısı = randint(1,100)
    DenemeSayısı = 0
    KullanıcıTahmini = None


    while not(KullanıcıTahmini == BilgisayarSayısı):
        DenemeSayısı += 1
        print(f"{DenemeSayısı}. Denemeniz")

        while True:
            KullanıcıTahmini = int(input("Lütfen Tahmininizi Giriniz.(Oyundan Çıkmak İçin 0' Basınız)"))
            geçerli_seçimler = list(range(101))
            if KullanıcıTahmini in geçerli_seçimler:
                break
            else:
                print("Geçersiz girdi, tekrar deneyiniz.")

        if KullanıcıTahmini == 0:
            break
        

        if KullanıcıTahmini > BilgisayarSayısı:
            print("Azaltın")
        elif KullanıcıTahmini < BilgisayarSayısı:
            print("Arttırın")
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
        SeçilenKelime = choice(hard_words)

    HarfList = list(SeçilenKelime)
    shuffle(HarfList)
    KarışıkKelime = ''.join(HarfList)

    print(f"Scrambled word: {KarışıkKelime}")

    while not(KelimeDenemeSayısı == 3):
        KelimeDenemeSayısı +=1
        YourGuess = input("Your guess: (Oyundan Çıkmak İçin 0' Basınız)").lower()

        if YourGuess == "0":
            break

        if SeçilenKelime == YourGuess:
            print(f"{KelimeDenemeSayısı}. Denemede Buldunuz. Tebrikler")
            break
        else:
            print(f"Incorrect. Please tr again ({3-KelimeDenemeSayısı} Hakkınız kaldı)")
    else:
        print("Başarısız oldunuz. üzgünüm")
        



OyunSeçimi = None
while not(OyunSeçimi == 4):
    print("Zeka Küpü - Mini Oyunlar")
    print("1 -> Taş Kağıt Makas")
    print("2 -> Sayı Tahmin Oyunu")
    print("3 -> Kelime Karıştırmaca")
    print("4 -> Çıkış")

    OyunSeçimi = int(input("Seçiminiz: "))


    if OyunSeçimi == 1:
        print("Taş Kağıt Makas Oyununa Hoş Geldiniz")
        while True:
            TasKağıtMakas()
            Karar =int(input("Bir daha oynamak için 1'e Ana Menüye Dönem İçin 2'ye basınız"))
            if Karar == 1:
                continue
            elif Karar == 2:
                break


    elif OyunSeçimi == 2:
        print("Sayı Tahmin Oyununa Hoş Geldiniz. 1 ile 100 Arasında Bir Sayı Tutunuz")
        while True:
            SayıTahminOyunu()
            Karar =int(input("Bir daha oynamak için 1'e Ana Menüye Dönem İçin 2'ye basınız"))
            if Karar == 1:
                continue
            elif Karar == 2:
                break

    elif OyunSeçimi == 3:
        print("Kelime Karıştırıcya HoşGeldiniz")
        while True:
            while True:
                ZorlukSeviyesi = int(input("Lütfen Zorluk Seviyesini Giriniz(5 ile 7 arasında)"))
                geçerli_seçimler = [5,6,7]
                if ZorlukSeviyesi in geçerli_seçimler:
                    break  
                else:
                    print("Geçersiz girdi, tekrar deneyiniz.")

            KelimeKarıştırmaca(ZorlukSeviyesi)
            Karar =int(input("Bir daha oynamak için 1'e Ana Menüye Dönem İçin 2'ye basınız"))
            if Karar == 1:
                continue
            elif Karar == 2:
                break

print("Programımızı Kullandığınız için teşekkürler. İyi Günler Dileriz :)")

