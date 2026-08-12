yas = int(input("Yaşınızı giriniz: "))
isim = input("İsminizi giriniz: ")

print("Merhaba " + isim + ", yaşınız " + str(yas) + " yaşında.")


say1 = int(input("1. sayıyı giriniz: "))
say2 = int(input("2. sayıyı giriniz: "))
toplam = say1 + say2
fark = say1 - say2
carpim = say1 * say2
bolum = say1 / say2
print("Toplam: " + str(toplam))
print("Fark: " + str(fark))
print("Çarpım: " + str(carpim))
print("Bölüm: " + str(bolum))


urun_fiyati = float(input("Ürün fiyatını giriniz: "))
adet = int(input("Adet sayısını giriniz: "))

toplam_fiyat = urun_fiyati * adet
print("Toplam Fiyat: " + str(toplam_fiyat))


order1 = float(input("Sipariş 1 fiyatını giriniz: "))
order2 = float(input("Sipariş 2 fiyatını giriniz: "))
order3 = float(input("Sipariş 3 fiyatını giriniz: "))

total_order = order1 + order2 + order3
print("Toplam Sipariş Tutarı: " + str(total_order))
print(type(total_order))
