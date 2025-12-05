# KİŞİSEL AJANDA / TO-DO LİSTESİ

gorevler = []

def gorev_ekle(isim):
    gorev = {"isim": isim, "tamamlandi": False}
    gorevler.append(gorev)
    print("Görev eklendi.")

def gorev_sil(isim):
    for g in gorevler:
        if g["isim"] == isim:
            gorevler.remove(g)
            print("Görev silindi.")
            return
    print("Görev bulunamadı.")

def gorev_tamamla(isim):
    for g in gorevler:
        if g["isim"] == isim:
            g["tamamlandi"] = True
            print("Görev tamamlandı olarak işaretlendi.")
            return
    print("Görev bulunamadı.")

def listele():
    if not gorevler:
        print("Liste boş.")
        return
    for g in gorevler:
        durum = "✔ Tamamlandı" if g["tamamlandi"] else "⏳ Bekliyor"
        print(f"- {g['isim']} --> {durum}")

while True:
    print("\n1) Görev Ekle\n2) Görev Sil\n3) Tamamla\n4) Listele\n5) Çıkış")
    secim = input("Seçim: ")

    if secim == "1":
        isim = input("Görev adı: ")
        gorev_ekle(isim)

    elif secim == "2":
        isim = input("Silinecek görev: ")
        gorev_sil(isim)

    elif secim == "3":
        isim = input("Tamamlanacak görev: ")
        gorev_tamamla(isim)

    elif secim == "4":
        listele()

    elif secim == "5":
        print("Program kapatıldı.")
        break
