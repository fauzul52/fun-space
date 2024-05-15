#hitung luas segitiga
def luas_segitiga():
    a = int(input("masukkan Alas segitiga: "))
    t= int(input("masukkan Tinggi segitiga: "))
    luas = a*t / 2
    print("Luas segitig adalah: ", luas)

luas_segitiga()

#hitung luas persegi panjang
def persegi_panjang():
    p = int(input("masukkan panjang persegi: "))
    l = int(input("masukkan luas persegi: "))
    luas = p*l 
    print("luas persegi panjang: ", luas)

persegi_panjang()