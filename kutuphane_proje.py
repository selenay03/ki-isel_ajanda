class kitap:
    def __init__(self, isim, yazar):
        self.isim = isim
        self.yazar = yazar

class kutuphane:
    def __init__(self):
        self.kitaplar = []

def kitap_ekle(self, isim, yazar):
    yeni = kitap(isim, yazar)
    self.kitaplar.append(yeni)
    print(f"{isim} eklendi.")


def kitap_sil(self, isim):
    for u in self.kitaplar:
        if u.isim == isim:
            self.kitaplar.remove(u)
            print(f"{isim} silindi.")
            return
        print("kitap bulunamadı.")

def kitap_guncelle(self, isim, yeni_yazar):
    for u in self.kitaplar:
        if u.isim == isim:
            self.yazar = yeni_yazar
            print(f"{isim} guncellendi.")
            return
        print("kitap bulunamadı.")


def kitap_listele(self):
    if not self.kitaplar:
        print("hiç kitap yok.")

    else:
        print("\n--- kitap listesi ---")
        for u in self.kitaplar:
            print(f"{u.isim}  -  {u.yazar} ")


#kullanıcı menüsü

def menu():
    kutuphane = kutuphane()


while True:
    print("n\--- kutuphane kitap takip sistemi ---")
    print("1- kitap ekle")
    print("2- kitap sil")
    print("3- kitap guncelle")
    print("4- kitapları listele")
    print("5- çıkış")


    secim = input("seçiminiz: ")

    if secim == "1":
        isim = input("kitap adı:")
        yazar = input("yazar: ")
        kutuphane.urun_sil(isim)

    elif secim == "2":
        isim = input("silinecek kitap: ")
        kutuphane.kitap_sil(isim)

    elif secim == "3":
        isim = input("güncellenecek kitap: ")
        yeni = input("yeni kitap: ")
        kutuphane.kitap_guncelle(isim, yeni)

    elif secim == "4":
        kutuphane.kitap_listele()


    elif secim == "5":
        print("programdan çıkılıyor...")
        break

    else:
        print("geçersiz seçim!")


    menu()
        