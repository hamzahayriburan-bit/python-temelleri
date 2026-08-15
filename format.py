name = 'John'
surname = 'Doe'
age = 25

print('My name is {} {} '.format(name, surname))
print('My name is {1} {0} '.format(name, surname)) # Burada format() fonksiyonu icinde index numaralarini kullanarak, name ve surname degiskenlerini ekrana yazdirir. {1} surname degiskenini, {0} ise name degiskenini temsil eder. Yani, ekrana "My name is Doe John" yazdirir.
print('My name is {s} {n} '.format(n=name, s=surname))
print("My name is {} {} and I am {} years old." .format(name, surname, age))
print("My name is {} {} and I am {} years old." .format(name, name, name))

result = 200 / 700
print('the result is {r:1.4}'.format(r=result)) # Burada format() fonksiyonu icinde result degiskenini ekrana yazdirir. Yani, ekrana "the result is 0.4" yazdirir.

print(f"My name is {name} {surname} and I am {age} years old.") # Bu yontem ile format() fonksiyonu kullanmadan, f-string yontemi ile degiskenleri ekrana yazdirir.
