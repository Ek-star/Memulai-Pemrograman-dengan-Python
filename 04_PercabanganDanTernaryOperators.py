# Percabangan
# Kasus pertama
ketersediaan = "Daging Ayam"
if ketersediaan == "Daging Ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

# Kasus kedua
nilai = 65

if nilai >= 80:
    print("Selamat! Anda mendapatkan nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

# Kasus ketiga
nilai = 81
perilaku = 'tidak baik'
if nilai >= 80 and perilaku == 'baik':
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != 'baik':
    print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
    print("Perbaiki lagi ya!")
else:
    print("Yuk belajar lebih giat lagi!")

# Ternary Operators
# (blok_kode_jia_benar) if (kondisi) else (blok_kode_jika_salah)
lulus = True
print("Selamat") if lulus else print("Pebaiki")

# Ternary Operators melibatkan Tuple
# (blok_kode_jika_salah) , (blok_kode_jika_benar)[kondisi]
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus." , "Selamat, Anda lulus!")[lulus]
print(kelulusan)