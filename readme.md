# Utility untuk upload kursus
Dikarenakan kendala, maka dalam memasukan kursus baru, harus melalui program ini, program ini akan otomatis memasukan kursus kedalam database. Program ini yang akan menghandle text-to speech dan base64 encode.

# Tutorial
## 1. Setup
Jalankan script ini untuk install semua package python yang diperlukan
```
pip install -r requirements.txt
```
Buka kode dan ganti credentials pada line 12-15
```
USERNAME = 'root'
PASSWORD = '100300'
URL = 'localhost'
DB = 'flexy'
```
## 2. Jalankan Script
PASTIKAN SERVER MYSQL BERJALAN SEBELUM DIRUN
```
py add_course.py
```
## 3. Masukkan Nama Kursus
Nama Kursus bebas, tidak ada batasan, max 100 karakter

## 4. Masukkan Foto thumbnail kursus
Akan muncul window yang menyuruh kalian pick file gambar, pilih gambar yang ingin dijadikan thumbail kursus

## 5. Masukkan Jumlah Modul kursus
Dalam Angka

## 6. Masukkan Bahasa Modul (Tujuan Untuk Text To Speech)
1. Indonesia, 2. Inggris. Kalau salah nanti audionya kocak (ibarat google translate inggris disuruh ngomong bahasa indonesia)

## 7. Pilih file .txt yang isinya teks yang akan diread dalam modul itu
Akan muncul window yang menyuruh kalian pick file, File harus txt.

## 8. Ulang langkah 6-7 untuk semua modul sesuai jumlah modul kursus

DONE. 
