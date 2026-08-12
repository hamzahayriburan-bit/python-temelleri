# Terminal ve Python Notları

Python öğrenirken kullandığım temel PowerShell ve Python komutları.

---

## 📁 PowerShell Komutları

### `cd`

Belirtilen klasöre geçer.

```powershell
cd klasor_adi
```

### `cd \`

Windows'ta bulunduğun sürücünün ana dizinine gider.

```powershell
cd \
```

Bir üst klasöre gitmek için:

```powershell
cd ..
```

### `mkdir`

Yeni bir klasör oluşturur.

```powershell
mkdir klasor_adi
```

### `ls`

Bulunduğun klasördeki dosya ve klasörleri listeler.

```powershell
ls
```

### `cls`

Terminal ekranını temizler.

```powershell
cls
```

### `clear`

Terminal ekranını temizlemek için kullanılabilir.

```powershell
clear
```

### `del`

Dosya silmek için kullanılır.

```powershell
del dosya.py
```

### `rmdir`

Klasör silmek için kullanılır.

```powershell
rmdir klasor_adi
```

### `code .`

Bulunduğun klasörü Visual Studio Code ile açar.

```powershell
code .
```

### `echo $null >>`

Boş bir dosya oluşturmak için kullanılabilir.

```powershell
echo $null >> uygulama.py
```

> PowerShell'e özgü bir kullanımdır.

---

# 🐍 Python

### `python`

Python'u çalıştırır.

```powershell
python
```

Bir Python dosyasını çalıştırmak için:

```powershell
python uygulama.py
```

### `py`

Windows'ta Python Launcher'ı çalıştırır.

```powershell
py uygulama.py
```

Python sürümünü kontrol etmek için:

```powershell
python --version
```

veya:

```powershell
py --version
```

---

# 🔢 Python Veri Tipleri

## `int`

Tam sayıları temsil eder.

```python
age = 20
number = 100
```

## `float`

Ondalıklı sayıları temsil eder.

```python
price = 19.99
number = 2.5
```

## `str`

Metinleri temsil eder.

```python
name = "Hamza"
```

## `bool`

Doğru veya yanlış değerlerini temsil eder.

```python
is_student = True
is_admin = False
```

---

# 🔍 `type()`

Bir değişkenin veri tipini öğrenmek için kullanılır.

```python
x = 10

print(type(x))
```

Çıktı:

```text
<class 'int'>
```

Örnek:

```python
x = 10
y = 10.5
name = "Hamza"
is_student = True

print(type(x))
print(type(y))
print(type(name))
print(type(is_student))
```

---

# ➕ Matematiksel Operatörler

| Operatör | İşlem | Örnek |
|---|---|---|
| `+` | Toplama | `10 + 5` |
| `-` | Çıkarma | `10 - 5` |
| `*` | Çarpma | `10 * 5` |
| `/` | Bölme | `10 / 5` |
| `**` | Üs alma | `2 ** 3` |
| `//` | Taban bölme | `10 // 3` |
| `%` | Mod alma | `10 % 3` |

Örnek:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)
```

---

# 💬 Yorum Satırları

## `#`

Python'da yorum satırı oluşturmak için kullanılır.

Yorum satırları Python tarafından çalıştırılmaz.

```python
# Bu bir yorum satırıdır.

name = "Hamza"  # Bu da bir yorumdur.
```

Yorumlar kodu açıklamak ve okunabilirliğini artırmak için kullanılır.
