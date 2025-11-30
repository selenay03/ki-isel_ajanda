# Tarla Ürün Takip Sistemi – Basit Python Projesi

# Ürün sınıfı (bir tane ürün tutmak için)
class Urun:
    def __init__(self, isim, miktar):
        self.isim = isim
        self.miktar = miktar

# Çiftlik sınıfı (ürünleri yönetmek için)
class Ciftlik:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, isim, miktar):
        yeni = Urun(isim, miktar)
        self.urunler.append(yeni)
        print(f"{isim} eklendi.")

    def urun_sil(self, isim):
        for u in self.urunler:
            if u.isim == isim:
                self.urunler.remove(u)
                print(f"{isim} silindi.")
                return
        print("Ürün bulunamadı.")

    def urun_guncelle(self, isim, yeni_miktar):
        for u in self.urunler:
            if u.isim == isim:
                u.miktar = yeni_miktar
                print(f"{isim} güncellendi.")
                return
        print("Ürün bulunamadı.")

    def urun_listele(self):
        if not self.urunler:
            print("Hiç ürün yok.")
        else:
            print("\n--- Ürün Listesi ---")
            for u in self.urunler:
                print(f"{u.isim} - {u.miktar} kg")

# Kullanıcı menüsü
def menu():
    ciftlik = Ciftlik()

    while True:
        print("\n--- Tarla Yönetim Sistemi ---")
        print("1- Ürün Ekle")
        print("2- Ürün Sil")
        print("3- Ürün Güncelle")
        print("4- Ürünleri Listele")
        print("5- Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("Ürün adı: ")
            miktar = input("Miktar (kg): ")
            ciftlik.urun_ekle(isim, miktar)

        elif secim == "2":
            isim = input("Silinecek ürün: ")
            ciftlik.urun_sil(isim)

        elif secim == "3":
            isim = input("Güncellenecek ürün: ")
            yeni = input("Yeni miktar: ")
            ciftlik.urun_guncelle(isim, yeni)

        elif secim == "4":
            ciftlik.urun_listele()

        elif secim == "5":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim!")

# Program başlatılıyor
menu()

