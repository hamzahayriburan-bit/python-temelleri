name = "John" # Index numaralari her zaman 0'dan baslar. Yani, "J" karakteri 0. index numarasina sahiptir.
surname = "Doe" # Index numaralarinda bu sefer sagdan sola dogru sayim yapilirsa. Yani, "e" karakteri -1,-2,-3... index numarasina sahiptir.
age = 36 

greeting = "My name and surname is " + name + " " + surname + " and \nI am " + str(age) + " years old."
length = len(greeting) # Stringin uzunlugunu hesaplar ve length degiskenine atar.


# print(greeting)
# print(greeting[0]) # Index numarasi 0 olan karakteri ekrana yazdirir.
# print(greeting[1]) # Index numarasi 1 olan karakteri ekrana yazdirir.
# print(greeting[3]) # Index numarasi 3 olan karakteri ekrana yazdirir.
# print(len(greeting)) # Stringin uzunlugunu hesaplar ve length degiskenine atar.
# print(greeting[length-1]) # Stringin son karakteri ekrana yazdirir.
# print(greeting[-1]) # Stringin son karakteri ekrana yazdirir. Greeting[length-1] ile ayni islemi yapar.
# print(greeting[2:5]) # Index numarasi 2 ile 5 arasindaki karakterleri ekrana yazdirir. (5 dahil degil)
# print(greeting[3:]) # Index numarasi 3 ile 16 arasindaki karakterleri ekrana yazdirir. (16 dahil degil)
# print(greeting[:16]) # Index numarasi 0 ile 16 arasindaki karakterleri ekrana yazdirir. (16 dahil degil)
# print(greeting[2:40:2]) # Index numarasi 2 ile 40 arasindaki karakterleri ekrana yazdirir. (40 dahil degil) Ve bu karakterleri 2'ser atlayarak ekrana yazdirir.
