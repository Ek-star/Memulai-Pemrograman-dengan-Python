# Mengubah Huruf Besar / Kecil
kata = "dicoding"
kata = kata.upper()
print(kata)

kata = "DICODING"
kata = kata.lower()
print(kata)

# Awalan dan Akhiran
print("Dicoding         ".rsplit())

print("       Dicoding          ".strip())

kata = "CodeCodeDicodingCodeCode"
print(kata.strip("Code"))

print('Dicoding Indonesia'.startswith('Dicoding'))

print('Dicoding Indonesia'.endswith("Dicoding"))

# Memisah dan Menggabung String
print('c'.join(["Dicoding" , "Indonesia" , '!']))

print('Dicoding Indonesia !'.split())
# Dipisah dan disimpan sebagai List

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# Mengganti Elemen String
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding" , "Pemrograman"))

# Pengecekan String
kata = "DICODING"
print(kata.isupper())

kata = "dicoding"
print(kata.islower())

kata = 'dicoding'
# Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.
print(kata.isalpha())

kata = 'dicoding123'
# Metode isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.
print(kata.isalnum())

print('123'.isdecimal())
# Metode isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik. Jika tidak, nilai False akan dikembalikan.

print('             '.isspace())
# Metode isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.

print('Dicoding Indonesia'.istitle())
# Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. Jika tidak, nilai False dikembalikan.

# Formatting pada String
text = 'Code'
tambah_number = text.zfill(5)
print(tambah_number)

print('Dicoding'.rjust(20))
print('Dicoding'.rjust(20, '!'))
# Metode rjust() berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.
print('Dicoding'.ljust(20, '!'))
# Selanjutnya adalah metode ljust(), metode ini adalah kebalikan dari metode rjust() yang bertujuan untuk membuat teks menjadi rata kiri.
print('Dicoding'.center(10, '-'))
# Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default. Anda juga bisa mengganti whitespace tersebut dengan karakter lain.

# String Literals
st1 = "Jum'at"
# Cara paling aman
st1 = 'Jum\'at'

# Raw String
# Python juga menyediakan cara untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan. Metode ini dinamakan raw strings. Umumnya, ia digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash. Untuk mengimplementasikan raw strings, sisipkan huruf r sebelum pembuka string.
print(r'Dicoding\tIndonesia')