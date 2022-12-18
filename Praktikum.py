# latihan menggunakan block try except untuk penangan exception


try:
    # membuat variable_1
    variable_1 = "Ini variable 1"
    # menampilkan variable yang salah
    print(variable1)  # seharusnya variable_1
    # memberitahu kesalahan pemanggilan variable dengan exception
except NameError as variable1:
    print(variable1)

try:
    # parameter x digunakan untuk membuat file
    f1 = open('filedemo2.txt', 'x')
    # menulis kata di difiledemo2.txt
    f1.write("Halo semuanya ini filedemo2 yang baru dibuat")
    print(f1.read())
    # jika filedemo2.txt sudah ada maka dilempar ke exception dibawah ini
except FileExistsError:
    raise FileExistsError("File dengan nama filedemo2 sudah ada.")

try:
    # membuka filedemo.txt dengan parameter r => yaitu membaca
    # disini kita panggil dengan nama yang salah agar dilempar ke execption
    f = open('filedem.txt', 'r')
    # membaca seluruh isi file
    print(f.read())
    # membaca satu baru dalam file dimulai baris pertama
    print(f.readline())
    # jika file tersebut tidak ada maka akan ditanganin oleh exception dan memberi ta
except FileNotFoundError as file_error:
    raise FileNotFoundError("File tidak ditemukan")

# menginput nim, fungsi input() selalu berupa string untuk type datanya
nim = input("Masukan NIM: ")
# jika nim bukan integer tipe datanya maka membangkitkan error dengan raise
if not type(nim) is int:
    # menangani bahwa nim wajib integer
    raise TypeError('Mohon maaf ni yee sebelumnya... nim kudu integer')
else:
    print(nim)
