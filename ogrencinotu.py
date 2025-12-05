def ortalama_hesapla(not1, not2):
    return (not1+not2) / 2


def durum_yazdir(ortalama):
    if ortalama >= 50:
      print("durum: geçtiniz")

    else:
       print("durum: kaldınız")




def main():
   print("=== not ortalaması hesaplama ===")

   not1 = float(input("1. notu gir: "))
   not2 = float(input("2. notu gir: "))

   ort = ortalama_hesapla(not1, not2)
   print("ortalama:"  , ort)

   durum_yazdir(ort)


   main()

