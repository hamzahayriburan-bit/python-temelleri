# Değişkenler ve Veri Tipleri

maas_ali = 5000
maas_ahmet = 4000
vergi = 0.27

print(maas_ali - (maas_ali * vergi))
print(maas_ahmet - (maas_ahmet * vergi))


# Değişken Tanımlama Kuralları

# Değişken isimleri rakam ile başlayamaz.

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)


# Büyük/küçük harf duyarlılığı vardır.
# number1 ve Number1 farklı değişkenlerdir.

age = 20
AGE = 30

print(age)
print(AGE)


# Türkçe karakterler teknik olarak kullanılabilir,
# ancak değişken isimlerinde kullanmamak daha iyi bir pratiktir.

yas = 20
_age = 20


# Veri tipleri

x = 1            # int
y = 2.0          # float
name = "Hamza"   # str
is_student = True  # bool


# Birden fazla değişken aynı satırda tanımlanabilir.

# x, y, name, is_student = (1, 2.0, "Hamza", True)


# String ve integer arasındaki fark

a = "10"
b = "5"

print(a + b)           # "105" -> string birleştirme
print(int(a) - int(b)) # 5 -> integer olarak çıkarma


# String birleştirme

first_name = "Emin"
last_name = "Yılmaz"

print(first_name + " " + last_name)
