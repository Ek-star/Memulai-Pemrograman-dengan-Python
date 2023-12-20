# Fungsi 
def mencari_luas_persegi_panjang(panjang, lebar):
  luas_persegi_panjang = panjang * lebar
  return luas_persegi_panjang

def greeting(nama , pesan):
  return "Halo, " + nama + " ! " + pesan

persegi_panjang_pertama = mencari_luas_persegi_panjang(5 , 10)
print (persegi_panjang_pertama)

print(greeting("Ekalma" , "Selamat pagi!"))
print(greeting(pesan = "Selamat sore!" , nama = "Ekalma"))

# Positional-Only
def penjumlahan(a , b , /):
  return a + b

print(penjumlahan(8 , 50))

# Keyword-Only
def greeting(* , nama , pesan):
  return "Halo, " + nama + " ! " + pesan

print(greeting(pesan = "Selamat sore!" , nama = "Ekalma"))

# Var-Positional (Variadic Positional Paraeter)
def hitung_total(*args):
  print(type(args))
  total = sum(args)
  return total

print(hitung_total(1 , 2 , 3))

# Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs):
  info = ""
  for key, value in kwargs.items():
    info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding" , usia="17" , pekerjaan="Python Programmer"))

# Fungsi Anonim (Lambda Expression)
mencari_luas_persegi_panjang = lambda panjang , lebar : panjang*lebar

print(mencari_luas_persegi_panjang(5 , 10))

# Variabel Global
a = 10
def add(b):
  result = a + b
  return result

bilanganPertama = add(20)
print(bilanganPertama)

# Variabel Lokal
def add(a , b):
  lokal_var = 5
  result = a + b - lokal_var
  return result

bilanganPertama = add(10,20)
print(bilanganPertama)