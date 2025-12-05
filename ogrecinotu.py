class student:
    def __init__(self):
        self.isim = isim
        self.notu = notu 

ogrenciler = []

while True:
    print("\n--- ogenci notu sistemi ---")
    print("1- ogrenci ekle")
    print("2- not güncelle")
    print("3- ogrecileri listele")
    print("4- not ortalaması hesapla")
    print("5- çıkış")

    secim = input("seçiminiz: ")

    if secim == "1":
        print("ogrenci ekleme işlemi seçildi.")

    elif secim == "2":
        print("not güncellemeişlemi seçildi.")

    elif secim == "3":
        print("ogrecileri listeleme işlemi seçildi.")

    elif secim == "5":
        print("programdan çıkılıyor...")
        break
    else:
        print("hatalı seçim! 1-5 arası bir değer gir.")